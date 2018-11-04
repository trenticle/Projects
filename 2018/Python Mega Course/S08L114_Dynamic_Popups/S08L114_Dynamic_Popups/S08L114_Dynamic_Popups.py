import folium
import pandas


mapDataFromTxt = pandas.read_csv('c:\\users\\trent\\desktop\\map\\volcanoes.txt')
latitudeFromMapData = list(mapDataFromTxt['LAT'])
longitudeFromMapData = list(mapDataFromTxt['LON'])
elevationFromMapData = list(mapDataFromTxt['ELEV'])
nameFromMapData = list(mapDataFromTxt['NAME'])
myMapFeatureGroup = folium.FeatureGroup(name='My Map')
map = folium.Map(location=[33.9409, -84.54818], zoom_start=12)

for latitudeInList, longitudeInList, nameInList, elevationInList in zip(latitudeFromMapData, longitudeFromMapData, nameFromMapData, elevationFromMapData):
    myMapFeatureGroup.add_child(folium.Marker(location=[latitudeInList, longitudeInList], popup=folium.Popup(nameInList, str(elevationInList)),icon=folium.Icon(color='red')))

map.add_child(myMapFeatureGroup)
map.save('c:\\users\\trent\\desktop\\map\\map4.html')


