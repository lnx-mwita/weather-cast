from django.shortcuts import render
from django.http import request
import requests
import json
from datetime import date,datetime

today = date.today()
time = datetime.now().strftime("%H:%M")
# Create your views here.
def home(request):
    return render(request,'index.html')

def weather(request):
    try:
        city = request.GET['search']
        api_key = 'fc7eaee4b8f30c7b2ebe505511239dbe'
        api = 'http://api.openweathermap.org/data/2.5/weather?q='+ city +'&appid='+api_key
        data = requests.get(api).json()
        kelvin = int(data['main']['temp'])
        degrees = (kelvin-273)
        date = today.strftime("%B %d, %Y")
        lat  = data['coord']['lat']
        long = data['coord']['lon']
        windspeed = int(data['wind']['speed'])*3.6
        direction = data['wind']['deg']
        humidity = data['main']['humidity']
        clouds = data['clouds']['all']
        country = data['sys']['country']
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        iconurl = "http://openweathermap.org/img/wn/"+icon+"@2x.png"
        return render(request, 'result.html', {
            'city':city,
            'position':['Position : ',lat,long],
            'temps':degrees,
            'date':date,
            'time':time,
            'windspeed':windspeed,
            'direction':direction,
            'humidity':humidity,
            'clouds':clouds,
            'country':country,
            'description':description,
            'icon':iconurl,
            })

    except ConnectionError:
       return render(request, 'index.html', {'Error':'**Connection might be down sorry**',})
    except ValueError:
         return render(request, 'index.html', {'valError':'',})
    except KeyError:
        return render(request, 'index.html', {'Error':'  ***Please enter a valid city ',})
    finally:
        pass






