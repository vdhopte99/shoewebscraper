from flask import Flask
from flask import render_template, make_response, request, flash
from webscraper import returnDrops
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='.')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.secret_key = "secretsneakerkey"
db = SQLAlchemy(app)

class shoeListing(db.Model):
    name = db.Column(db.String(150), nullable=False, primary_key=True)
    retail = db.Column(db.Integer, nullable=True)
    resale = db.Column(db.Integer, nullable=True)
    profit = db.Column(db.Integer, nullable=True)
    image = db.Column(db.Text, nullable=True)
    month = db.Column(db.String(10), nullable=False)
    date = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"shoeListing('{self.name}', '{self.retail}', '{self.resale}')"

@app.route('/')
def home():
    html = render_template('home.html')
    response = make_response(html)
    return response

@app.route('/getDrops', methods=['GET'])
def getDrops():
    month = request.args.get('month')
    results = shoeListing.query.filter_by(month=month).all()

    if len(results) == 0:
        try:
            shoes = returnDrops(month)

            for shoe in shoes:
                listing = shoeListing(name=shoe['name'], retail=shoe['retail'], resale=shoe['resale'], profit=shoe['profit'], month=month, date=shoe['date'], image=shoe['image'])
                db.session.add(listing)
            db.session.commit()

            results = shoeListing.query.filter_by(month=month).all()
        except:
            return("<h3 style='color: rgb(255, 123, 123);'>Sorry :/ upcoming sneakers for this month cannot be displayed right now, please try again later<h3>")



    html = "<table class='table table-hover table-dark' style='text-align: center; overflow: scroll;' id='shoelist'>" + \
                "<caption>Last updated on:</caption>" + \
                "<th style'color: rgb(255, 123, 123);'>Name:</th>" + \
                "<th style='color: rgb(255, 123, 123);'>Retail Price:</th>" + \
                "<th style='color: rgb(255, 123, 123);'>Resale Price:</th>" + \
                "<th style='color: rgb(255, 123, 123);'>Potential Profit:</th>" + \
                "<th></th>"

    for result in results:
        html += "<tr><td>" + result.name + "</td>"

        if result.retail == 0:
            html += "<td>Unavailable</td>"
        else:
            html += "<td>$" + str(result.retail) + "</td>"

        if result.resale == 0:
            html += "<td>Unavailable</td>" 
        else:
            html += "<td>$" + str(result.resale) + "</td>"

        if result.profit == None or result.retail == 0 or result.resale == 0:
            html += "<td style='color: rgb(255, 255, 125);'><strong><u>Unavailable</u></strong></td>"
        elif result.profit > 0:
            html += "<td style='color: rgb(96, 235, 96);'><strong><u>$" + str(result.profit) + "</u></strong></td>"
        else:
            html += "<td style='color: rgb(255, 123, 123);'><strong><u>$" + str(result.profit) + "</u></strong></td>"

        if result.image != "https://images.solecollector.com/complex/image/upload/v1557176412/SC_Logo_Globe_TM_Blue_20190506-01-01-01_urcggx.svg":
            html += "<td><img src='" + result.image + "'></td>" + \
                    "</tr>"
        else:
            html += "<td>Image Unreleased</td>" + \
                    "</tr>"
    
    html += "</table>"

    response = make_response(html)
    return response

@app.route('/updateDrops', methods=['GET'])
def updateDrops():
    month = request.args.get('month')

    try:
        updatedShoes = returnDrops(month)
    except:
        results = shoeListing.query.filter_by(month=month).all()

        if len(results) == 0:
            return("<h3 style='color: rgb(255, 123, 123);'>Sorry :/ upcoming sneakers for this month cannot be displayed right now, please try again later<h3>")

        html = "<div class='alert alert-danger alert-dismissible fade show' role='alert'>Sorry, an error occurred while updating sneakers. Please try again later." + \
               "<button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span>" + \
               "</button></div>"
 
        html += "<table class='table table-hover table-dark' style='text-align: center; overflow: scroll;' id='shoelist'>" + \
                "<th style'color: rgb(255, 123, 123);'>Name:</th>" + \
                "<th style='color: rgb(255, 123, 123);'>Retail Price:</th>" + \
                "<th style='color: rgb(255, 123, 123);'>Resale Price:</th>" + \
                "<th style='color: rgb(255, 123, 123);'>Potential Profit:</th>" + \
                "<th></th>"

        for result in results:
            html += "<tr><td>" + result.name + "</td>"

            if result.retail == 0:
                html += "<td>Unavailable</td>"
            else:
                html += "<td>$" + str(result.retail) + "</td>"

            if result.resale == 0:
                html += "<td>Unavailable</td>" 
            else:
                html += "<td>$" + str(result.resale) + "</td>"

            if result.profit == None or result.retail == 0 or result.resale == 0:
                html += "<td style='color: rgb(255, 255, 125);'><strong><u>Unavailable</u></strong></td>"
            elif result.profit > 0:
                html += "<td style='color: rgb(96, 235, 96);'><strong><u>$" + str(result.profit) + "</u></strong></td>"
            else:
                html += "<td style='color: rgb(255, 123, 123);'><strong><u>$" + str(result.profit) + "</u></strong></td>"

            if result.image != "https://images.solecollector.com/complex/image/upload/v1557176412/SC_Logo_Globe_TM_Blue_20190506-01-01-01_urcggx.svg":
                html += "<td><img src='" + result.image + "'></td>" + \
                        "</tr>"
            else:
                html += "<td>Image Unreleased</td>" + \
                        "</tr>"
        
        html += "</table>"

        response = make_response(html)
        return response

    counter = 0
    for shoe in updatedShoes:
        try:
            result = shoeListing.query.filter_by(name=shoe['name']).one()

            updated = False
            if result.retail != shoe['retail']:
                result.retail = shoe['retail']
                updated = True
            if result.resale != shoe['resale'] and shoe['resale'] != 0:
                result.resale = shoe['resale']
                updated = True
            result.profit = result.resale - result.retail
            if result.month != month:
                result.month = month
                updated = True
            if result.date != shoe['date']:
                result.date = shoe['date']
                updated = True
            db.session.commit()
            if updated:
                counter += 1
        except:
            listing = shoeListing(name=shoe['name'], retail=shoe['retail'], resale=shoe['resale'], profit=shoe['profit'], month=month, date=shoe['date'], image=shoe['image'])
            db.session.add(listing)
            db.session.commit()
            counter += 1
        
    results = shoeListing.query.filter_by(month=month).all()

    html = "<div class='alert alert-success alert-dismissible fade show' role='alert'>Successfully updated "+ str(counter) + " sneakers." + \
               "<button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span>" + \
               "</button></div>"

    html += "<table class='table table-hover table-dark' style='text-align: center; overflow: scroll;' id='shoelist'>" + \
                "<caption>Last updated on:</caption>" + \
                "<th style'color: rgb(255, 123, 123);'>Name:</th>" + \
                "<th style='color: rgb(255, 123, 123);'>Retail Price:</th>" + \
                "<th style='color: rgb(255, 123, 123);'>Resale Price:</th>" + \
                "<th style='color: rgb(255, 123, 123);'>Potential Profit:</th>" + \
                "<th></th>"

    for result in results:
        html += "<tr><td>" + result.name + "</td>"

        if result.retail == 0:
            html += "<td>Unavailable</td>"
        else:
            html += "<td>$" + str(result.retail) + "</td>"

        if result.resale == 0:
            html += "<td>Unavailable</td>" 
        else:
            html += "<td>$" + str(result.resale) + "</td>"

        if result.profit == None or result.retail == 0 or result.resale == 0:
            html += "<td style='color: rgb(255, 255, 125);'><strong><u>Unavailable</u></strong></td>"
        elif result.profit > 0:
            html += "<td style='color: rgb(96, 235, 96);'><strong><u>$" + str(result.profit) + "</u></strong></td>"
        else:
            html += "<td style='color: rgb(255, 123, 123);'><strong><u>$" + str(result.profit) + "</u></strong></td>"

        if result.image != "https://images.solecollector.com/complex/image/upload/v1557176412/SC_Logo_Globe_TM_Blue_20190506-01-01-01_urcggx.svg":
            html += "<td><img src='" + result.image + "'></td>" + \
                    "</tr>"
        else:
            html += "<td>Image Unreleased</td>" + \
                    "</tr>"
    
    html += "</table>"

    response = make_response(html)
    return response

if __name__ == '__main__':
    app.run(debug=True)