import requests
import urllib.parse
import folium

lst = ['Челябинск, улица Братьев Кашириных, 131Б ', 'Челябинск, улица Труда, 19 ', 'Челябинск, 2-я Бугурусланская улица, 1 ', 'Челябинск, улица Суркова ', 'Челябинск, улица Университетская Набережная, 32А ', 'Челябинск, Краснопольский проспект, 1 ', 'Челябинск, улица Братьев Кашириных, 97 ', 'Челябинск, Абразивная улица, 50 ', 'Челябинск, Гранитная улица ', 'Челябинск, проспект Ленина, 54 к2 ', 'Челябинск, Южноуральская улица ', 'Челябинск, Каслинская улица, 44 ', 'Челябинск, улица Комарова, 110 ', 'Челябинск, улица Самохина, 72 ', 'Челябинск, улица Комарова, 110 ', 'Челябинск, улица Александра Шмакова, 17А ', 'Челябинск, улица Блюхера, 8А ', 'Челябинск, улица Курчатова, 23Б ', 'Копейск, проспект Победы, 72а/1 ', 'Челябинск, Рабоче-Колхозная улица, 33 ']
latitude = []
longitude = []
for address in lst:
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
    response = requests.get(url).json()
    if response != []:
        latitude.append(float(response[0]["lat"]))
        longitude.append(float(response[0]["lon"]))

max_latitude = max(latitude)
max_longitude = max(longitude)

map = folium.Map(location=[(max_latitude),(max_longitude)], zoom_start = 10)

for lat, lon in zip(latitude, longitude):
    folium.Marker(location=[lat, lon] , icon=folium.Icon(color = 'gray')).add_to(map)

map.save("map.html")
