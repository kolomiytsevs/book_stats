import config
import urllib.request, urllib.parse, urllib.error
import json

maps_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

'address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY'

address = input('please enter and address')

request_url = maps_url + urllib.parse.urlencode({'address': address, 'key': config.MAPS_API_KEY})
# + urllib.parse.urlencode({'key': config.MAPS_API_KEY})

print('retrieving url', request_url)

data = urllib.request.urlopen(request_url).read().decode()
print('data length:', len(data))
location_data = json.loads(data)

print(location_data['results'][0]['formatted_address'])