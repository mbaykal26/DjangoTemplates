from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

def index(request):
    #return HttpResponse("Main Page")
    return render(request, "template_app/first.html")

def weather_view(request):
    weather_dictionary = {
        "istanbul": "30",
         "amsterdam": "20",
         "paris": [-23, 23, 45, 32, 23],
         "rome": {"morning": 10, "evening": 20},
         "user_premium": True,
         "test": "Murat Baykal Television"
         }
    return render(request, "template_app/weather.html",context = weather_dictionary)