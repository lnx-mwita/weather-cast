from django.shortcuts import render
from django.http import request
import requests
import json



# Create your views here.
def home(request):
    return render(request,'index.html')

def weather(request):
    global api
    try:
        city = request.GET['search']
        api_key = 'fc7eaee4b8f30c7b2ebe505511239dbe'
        api = 'http://api.openweathermap.org/data/2.5/weather?q='+ city +'&appid='+api_key
        data = requests.get(api).json()
        kelvin = int(data['main']['temp'])
        degrees = (kelvin-273)
        lat  = data['coord']['lat']
        long = data['coord']['lon']
        return render(request, 'index.html', {
            'city':city,
            'position':[lat,long],
            'temps':degrees})

    except ConnectionError:
       return render(request, 'index.html', {'city':'Connection might be down sorry',})
    except ValueError:
         return render(request, 'index.html', {'city':city,})
    except KeyError:
        return render(request, 'index.html', {'city':'Please enter a valid city ',})
    finally:
        pass






