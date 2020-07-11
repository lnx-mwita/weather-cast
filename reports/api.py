import requests
import json

def converter(fahrenheit):
     degrees = (fahrenheit-273)
     return degrees

city = 'mombasa'
api_key = 'fc7eaee4b8f30c7b2ebe505511239dbe'
api = 'http://api.openweathermap.org/data/2.5/weather?q='+ city +'&appid='+api_key

#request = requests.get(api).json()
#lat  = request['coord']['lat']
#long = request['coord']['lon']
#long, lat


#print (converter(request['main']['temp']))


api_key = 'fc7eaee4b8f30c7b2ebe505511239dbe'
api = 'http://api.openweathermap.org/data/2.5/weather?q='+ city +'&appid='+api_key
data = requests.get(api).json()
kelvin = int(data['main']['temp'])
degrees = (kelvin-273)
lat  = data['coord']['lat']
long = data['coord']['lon']
lat,long
print(degrees)

