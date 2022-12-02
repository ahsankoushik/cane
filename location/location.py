
from requests import request

# parameter for urlopen
url_geo_location = "http://ip-api.com/json/"
web_response=request("GET",url_geo_location)
json_data=web_response.json()

lat=json_data["lat"]
lon=json_data["lon"]
# print(lat)
# print(lon)

# For test Dania Counity center lat long used
lat=23.701564084669528
lon=90.44793859321011

url_address="https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat="+str(lat)+"&lon="+str(lon)+"&accept-language=en-US"
web_response=request("GET",url_address)
json_data=web_response.json()

# print(json_data)

address=json_data["display_name"]

print(address)