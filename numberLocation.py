import phonenumbers
import folium

from myNumber import number

from phonenumbers import geocoder

key = "1493541e60e04957aeb04364589f8dc9"

samNumber = phonenumbers.parse(number)

yourlca = geocoder.description_for_number(samNumber, "en")
print(yourlca)



## get service povider

from phonenumbers import carrier

service_povider = phonenumbers.parse(number)
print(carrier.name_for_number(service_povider, "en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)

query = str(yourlca)

result = geocoder.geocode(query)

lat = result[0]['geometry']['lat']

lng = result[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location[lat, lng], zoom_start = 9)

folium.Marker([lat, lng],popup = yourlca).add_to((myMap))

##save Html file

myMap.save("loca.html")
