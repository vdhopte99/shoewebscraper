from flask import Flask
from flask import render_template, make_response, request
from webscraper import returnDrops

app = Flask(__name__, template_folder='.')

# shoes = [{'name': 'Adidas Harden Vol. 5 Crystal White/Cloud White/Royal Blue', 'retail': 130, 'image': 'https://images.solecollector.com/complex/image/upload/c_fill,f_auto,fl_lossy,g_auto,h_200,q_auto,w_350/amc35hlax4cfqo9hrkqh.jpg', 'resale': 0, 'profit': 0, 'date': '4'}, 
# {'name': 'Jordan Why Not Zer0.4 "Upbringing"', 'retail': 130, 'image': 'https://images.solecollector.com/complex/image/upload/c_fill,f_auto,fl_lossy,g_auto,h_200,q_auto,w_350/uoo06cp9cs9rid86ovbf.jpg', 'resale': 0, 'profit': 0, 'date': '6'}, 
# {'name': 'Nike LeBron 18 "The Chosen 2"', 'retail': 225, 'image': 'https://images.solecollector.com/complex/image/upload/c_fill,f_auto,fl_lossy,g_auto,h_200,q_auto,w_350/m8xleffcykok0xl2j2cy.jpg', 'resale': 0, 'profit': 0, 'date': '7'}, 
# {'name': 'Air Jordan 35 "Bred"', 'retail': 180, 'image': 'https://images.solecollector.com/complex/image/upload/c_fill,f_auto,fl_lossy,g_auto,h_200,q_auto,w_350/mr3ceoxryngbed1tezvd.jpg', 'resale': 0, 'profit': 0, 'date': '8'}, 
# {'name': 'Adidas ZX 8000 "Vieux Lyons"', 'retail': 140, 'image': 'https://images.solecollector.com/complex/image/upload/c_fill,f_auto,fl_lossy,g_auto,h_200,q_auto,w_350/epq2wu6mg3vrretycobq.jpg', 'resale': 0, 'profit': 0, 'date': '8'}, 
# {'name': 'Undefeated x Nike Air Max 97 "White"', 'retail': 180, 'image': 'https://images.solecollector.com/complex/image/upload/c_fill,f_auto,fl_lossy,g_auto,h_200,q_auto,w_350/v0jq34c3aofmirqtchvz.jpg', 'resale': 0, 'profit': 0, 'date': '8'}, 
# {'name': 'Air Jordan 1 Retro High OG "Volt Gold"', 'retail': 170, 'image': 'https://images.solecollector.com/complex/image/upload/c_fill,f_auto,fl_lossy,g_auto,h_200,q_auto,w_350/omf51c5jrwck1rkam9h0.jpg', 'resale': 0, 'profit': 0, 'date': '9'}, 
# {'name': 'New Balance 57/40 Black', 'retail': 120, 'image': 'https://images.solecollector.com/complex/image/upload/c_fill,f_auto,fl_lossy,g_auto,h_200,q_auto,w_350/hd1weykrhoztcazmh9cx.jpg', 'resale': 0, 'profit': 0, 'date': '9'}, 
# {'name': 'Nike Dunk Low "UNLV"', 'retail': 100, 'image': 'https://images.solecollector.com/complex/image/upload/c_fill,f_auto,fl_lossy,g_auto,h_200,q_auto,w_350/hddk2gwqrywihyzlvimm.jpg', 'resale': 0, 'profit': 0, 'date': '14'}, 
# {'name': 'Nike Dunk Low White/Black-White', 'retail': 100, 'image': 'https://images.solecollector.com/complex/image/upload/c_fill,f_auto,fl_lossy,g_auto,h_200,q_auto,w_350/fw5wdyl0jiqgjzgvxcwu.jpg', 'resale': 0, 'profit': 0, 'date': '14'}, 
# {'name': 'Nike Dunk High Women\'s "Football Grey"', 'retail': 120, 'image': 'https://images.solecollector.com/complex/image/upload/c_fill,f_auto,fl_lossy,g_auto,h_200,q_auto,w_350/q6yrryaahuaqbouc6j0l.jpg', 'resale': 0, 'profit': 0, 'date': '14'}, 
# {'name': 'Nike Dunk Low Women\'s "Coast"', 'retail': 100, 'image': 'https://images.solecollector.com/complex/image/upload/c_fill,f_auto,fl_lossy,g_auto,h_200,q_auto,w_350/p8vtfrwuryz4aasv0szt.jpg', 'resale': 0, 'profit': 0, 'date': '14'}, 
# {'name': 'Nike Dunk High "Vast Grey"', 'retail': 120, 'image': 'https://images.solecollector.com/complex/image/upload/c_fill,f_auto,fl_lossy,g_auto,h_200,q_auto,w_350/pcnlq8g7rtymlovwrca8.jpg', 'resale': 0, 'profit': 0, 'date': '14'},
# {'name': 'Peanuts x Puma Future Rider Puma Black-Puma White-High Risk Red', 'retail': 110, 'image': 'https://images.solecollector.com/complex/image/upload/c_fill,f_auto,fl_lossy,g_auto,h_200,q_auto,w_350/pilgdhhifv7t34nbm6ho.jpg', 'resale': 0, 'profit': 0, 'date': '15'}, 
# {'name': 'Nike Air Force 1 Low "Rayguns"', 'retail': 110, 'image': 'https://images.solecollector.com/complex/image/upload/c_fill,f_auto,fl_lossy,g_auto,h_200,q_auto,w_350/zrc3idnzhztpkguzpyel.jpg', 'resale': 0, 'profit': 0, 'date': '15'}, 
# {'name': 'Nike Air Raid "Rayguns"', 'retail': 145, 'image': 'https://images.solecollector.com/complex/image/upload/c_fill,f_auto,fl_lossy,g_auto,h_200,q_auto,w_350/pzxuzgicb0wqlzix1tfa.jpg', 'resale': 0, 'profit': 0, 'date': '15'}, 
# {'name': 'Nike Blazer Mid "Rayguns"', 'retail': 110, 'image': 'https://images.solecollector.com/complex/image/upload/c_fill,f_auto,fl_lossy,g_auto,h_200,q_auto,w_350/h6ngjjh3pe9nhhjdsgpe.jpg', 'resale': 0, 'profit': 0, 'date': '15'}, 
# {'name': 'Peanuts x Puma Ralph Sampson Puma White-Peacoat', 'retail': 110, 'image': 'https://images.solecollector.com/complex/image/upload/c_fill,f_auto,fl_lossy,g_auto,h_200,q_auto,w_350/yjlm3tfmp80eewapncto.jpg', 'resale': 0, 'profit': 0, 'date': '15'}, 
# {'name': 'Adidas Yeezy Boost 380 "Yecoraite"', 'retail': 230, 'image': 'https://images.solecollector.com/complex/image/upload/c_fill,f_auto,fl_lossy,g_auto,h_200,q_auto,w_350/epsxsxhdga9rqxd1kgf3.jpg', 'resale': 0, 'profit': 0, 'date': '16'}, 
# {'name': 'Air Jordan 13 Retro "Starfish"', 'retail': 190, 'image': 'https://images.solecollector.com/complex/image/upload/c_fill,f_auto,fl_lossy,g_auto,h_200,q_auto,w_350/ryzf4tiyqwkkkjkrdqiy.jpg', 'resale': 0, 'profit': 0, 'date': '16'}, 
# {'name': 'Nike PG 5 Black/White', 'retail': 0, 'image': 'https://images.solecollector.com/complex/image/upload/c_fill,f_auto,fl_lossy,g_auto,h_200,q_auto,w_350/gtc4yvxo3wjoqknqnsqt.jpg', 'resale': 0, 'profit': 0, 'date': '21'}, 
# {'name': 'Notre x Nike Dunk High "Tan"', 'retail': 150, 'image': 'https://images.solecollector.com/complex/image/upload/c_fill,f_auto,fl_lossy,g_auto,h_200,q_auto,w_350/ddvw4d5yruoh4fbeghmd.jpg', 'resale': 0, 'profit': 0, 'date': '21'}, 
# {'name': 'Air Jordan 4 Retro Women\'s "Starfish"', 'retail': 190, 'image': 'https://images.solecollector.com/complex/image/upload/c_fill,f_auto,fl_lossy,g_auto,h_200,q_auto,w_350/fzfpb8meupvn9oiyyqfw.jpg', 'resale': 215, 'profit': 25, 'date': '22'},
# {'name': 'Nike SB Dunk Low "Street Hawker"', 'retail': 110, 'image': 'https://images.solecollector.com/complex/image/upload/c_fill,f_auto,fl_lossy,g_auto,h_200,q_auto,w_350/hd4dtbd9adb7em0oruig.jpg', 'resale': 673, 'profit': 563, 'date': '22'}, 
# {'name': 'Air Jordan 5 Retro Low "Chinese New Year"', 'retail': 215, 'image': 'https://images.solecollector.com/complex/image/upload/c_fill,f_auto,fl_lossy,g_auto,h_200,q_auto,w_350/e0wyu158jrtxfvaehpjs.jpg', 'resale': 244, 'profit': 29, 'date': '23'}, 
# {'name': 'Notre x Nike Dunk High "Midnight Navy"', 'retail': 150, 'image': 'https://images.solecollector.com/complex/image/upload/c_fill,f_auto,fl_lossy,g_auto,h_200,q_auto,w_350/liplp8mhyvzuhbemoyoy.jpg', 'resale': 0, 'profit': 0, 'date': '23'},
# {'name': 'Nike SB Dunk Low "Court Purple"', 'retail': 100, 'image': 'https://images.solecollector.com/complex/image/upload/c_fill,f_auto,fl_lossy,g_auto,h_200,q_auto,w_350/sz2aoub1q4liwmxwagvp.jpg', 'resale': 298, 'profit': 198, 'date': '23'}, 
# {'name': 'Adidas Yeezy Boost 700 "Sun"', 'retail': 240, 'image': 'https://images.solecollector.com/complex/image/upload/c_fill,f_auto,fl_lossy,g_auto,h_200,q_auto,w_350/dip19zfkzpb7pkgqrtjr.jpg', 'resale': 460, 'profit': 220, 'date': '23'}, 
# {'name': 'Adidas Ultra Boost 21 Cloud White/Core Black/Solar Yellow', 'retail': 180, 'image': 'https://images.solecollector.com/complex/image/upload/c_fill,f_auto,fl_lossy,g_auto,h_200,q_auto,w_350/lljmlky6kjiovhjf9uup.jpg', 'resale': 0, 'profit': 0, 'date': '28'}, 
# {'name': 'Nike Kyrie 7 "Rayguns"', 'retail': 130, 'image': 'https://images.solecollector.com/complex/image/upload/c_fill,f_auto,fl_lossy,g_auto,h_200,q_auto,w_350/j9j1wmjqaawtwmupjuuh.jpg', 'resale': 275, 'profit': 145, 'date': '29'}, 
# {'name': 'Air Jordan 9 Retro "University Gold"', 'retail': 190, 'image': 'https://images.solecollector.com/complex/image/upload/c_fill,f_auto,fl_lossy,g_auto,h_200,q_auto,w_350/af0kepswvjne7ky3che2.jpg', 'resale': 259, 'profit': 69, 'date': '30'}, 
# {'name': 'Nike LeBron 18 "Dunkman"', 'retail': 200, 'image': 'https://images.solecollector.com/complex/image/upload/c_fill,f_auto,fl_lossy,g_auto,h_200,q_auto,w_350/jlvciooaj25zehz2du7n.jpg', 'resale': 172, 'profit': -28, 'date': '30'}, 
# {'name': 'Air Jordan 1 Retro Low OG "Chinese New Year"', 'retail': 0, 'image': 'https://images.solecollector.com/complex/image/upload/c_fill,f_auto,fl_lossy,g_auto,h_200,q_auto,w_350/jaz2mpnkdrijyqc1kuwa.jpg', 'resale': 314, 'profit': 0, 'date': '31'}]

@app.route('/')
def home():
    # shoes = returnDrops("January")
    html = render_template('home.html')
    response = make_response(html)
    return response

@app.route('/getDrops', methods=['GET'])
def getDrops():
    month = request.args.get('month')
    shoes = returnDrops(month)

    html = "<table class='table table-hover table-dark' style='text-align: center; overflow: scroll;' id='shoelist'>" + \
                "<caption>Last updated on:</caption>" + \
                "<th>Name:</th>" + \
                "<th>Retail Price:</th>" + \
                "<th>Resale Price:</th>" + \
                "<th>Potential Profit:</th>" + \
                "<th></th>"

    for shoe in shoes:
        html += "<tr><td>" + shoe['name'] + "</td>"

        if shoe['retail'] == 0:
            html += "<td style='color: rgb(255, 255, 125);'>Unavailable</td>"
        else:
            html += "<td>$" + str(shoe['retail']) + "</td>"

        if shoe['resale'] == 0:
            html += "<td style='color: rgb(255, 255, 125);'>Unavailable</td>" + \
                    "<td style='color: rgb(255, 255, 125);'>Unavailable</td>"
        else:
            html += "<td>$" + str(shoe['resale']) + "</td>"

        if shoe['profit'] == None:
            html += "<td style='color: rgb(255, 255, 125);'>Unavailable</td>"
        elif shoe['profit'] > 0:
            html += "<td style='color: rgb(96, 235, 96);'>$" + str(shoe['profit']) + "</td>"
        else:
            html += "<td style='color: rgb(96, 235, 96);'>$" + str(shoe['profit']) + "</td>"
        
        html += "<td><img src='" + shoe['image'] + "'></td>" + \
                "</tr>"
    
    html += "</table>"

    response = make_response(html)
    return response

if __name__ == '__main__':
    app.run(debug=True)