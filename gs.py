
import requests
import json

key = "6d33086fafdb21"
lat = "-37.870662"
lon = "144.9803321"
url = "https://us1.locationiq.com/v1/reverse.php?key="+key+"&lat="+lat+"&lon="+lon+"&format=json"
'''
data = {
    'key': '6d33086fafdb21',
    'lat': '-37.870662',
    'lon': '144.9803321',
    'format': 'json'
}
'''
response = requests.get(url)
y=json.loads(response.text)
print("ISS is in the state",y['address']['state'])
print("of",y['address']['country'], )