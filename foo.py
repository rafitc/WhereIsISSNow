import urllib.request
import json
import requests

req = urllib.request.Request("http://api.open-notify.org/iss-now.json")
with urllib.request.urlopen(req) as response:

	obj = json.loads(response.read())
	lat = obj['iss_position']['latitude']
	lon = obj['iss_position']['longitude']

key = "6d33086fafdb21"
url = "https://us1.locationiq.com/v1/reverse.php?key="+key+"&lat="+lat+"&lon="+lon+"&format=json"


response = requests.get(url)
y=json.loads(response.text)
print("ISS is in the state",y['address']['state'])
print("of",y['address']['country'], )