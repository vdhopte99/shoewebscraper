from django.shortcuts import render
from django.http import HttpResponse

shoes = [
    {
        "name": "Shoe 1",
        "retail": 100,
        "image": "https://images.solecollector.com/complex/image/upload/c_fill,f_auto,fl_lossy,g_auto,h_200,q_auto,w_350/amc35hlax4cfqo9hrkqh.jpg",
        "resale": 200,
        "profit": 100
    },
    {
        "name": "Shoe 2",
        "retail": 100,
        "image": "https://images.solecollector.com/complex/image/upload/c_fill,f_auto,fl_lossy,g_auto,h_200,q_auto,w_350/uoo06cp9cs9rid86ovbf.jpg",
        "resale": None,
        "profit": None
    }
]

def home(request):
    context = {
        "shoes": shoes
    }

    return render(request, 'shoelistings/home.html', context)
