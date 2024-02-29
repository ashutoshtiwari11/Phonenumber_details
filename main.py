import phonenumbers
from phonenumbers import geocoder, carrier, timezone

# Replace 'number' with the actual phone number you want to check
number = "+91***********"

pepnumber = phonenumbers.parse(number, None)
location = geocoder.description_for_number(pepnumber, "en")
print("Location:", location)

service_pro = phonenumbers.parse(number, "en")
print("Carrier:", carrier.name_for_number(service_pro, "en"))
print(timezone.time_zones_for_geographical_number(service_pro))

#installed open cage as third party library for exact locatuon
from opencage.geocoder import OpenCageGeocode

key = "68**********************"
#get your own api key from geocoder
geocoder = OpenCageGeocode(key)
query = str(location)
results= geocoder.geocode(query)
print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

import folium 

mymap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(mymap)

mymap.save("mylocation.html") 
