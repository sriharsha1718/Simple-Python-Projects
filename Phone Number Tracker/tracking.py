#Python Code to find Country of Mobile Number and Visualize the Country Map using Folium
import phonenumbers 
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

#Mobile Number should be given here
number = "+91XXXXXXXXXX"

phoneNumber = phonenumbers.parse(number)
if phonenumbers.is_valid_number(phoneNumber):

	location = geocoder.description_for_number(phoneNumber, "en")
	print(location)

	print(carrier.name_for_number(phoneNumber, "en"))

	print(timezone.time_zones_for_number(phoneNumber))
else:
	print("Phone number is not valid. :(")


import opencage
from opencage.geocoder import OpenCageGeocode

key = "95179a72b6794e09addb48181a460974"
geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)
# print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print(lat, lng)

import folium
myMap = folium.Map(location = [lat, lng], zoom_start = 9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")