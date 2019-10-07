import urllib.request



with urllib.request.urlopen("http://api.open-notify.org/iss-now.json") as response:
	obj = json.loads(response.read())
	latitude = obj['iss_position']['latitude']
	longitude = obj['iss_position']['longitude']
	#print("latitude",longitude)
	#print (obj['iss_position']['latitude']) # obj['data']['iss_position']['latitude'])
	print (obj['iss_position']['longitude'])