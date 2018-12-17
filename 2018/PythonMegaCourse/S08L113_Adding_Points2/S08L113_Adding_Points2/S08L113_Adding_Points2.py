import folium
import pandas


mapDataFromTxt = pandas.read_csv('c:\\users\\trent\\desktop\\map\\volcanoes.txt')
latitudeFromMapData = list(mapDataFromTxt['LAT'])
longitudeFromMapData = list(mapDataFromTxt['LON'])
myMapFeatureGroup = folium.FeatureGroup(name='My Map')
map = folium.Map(location=[33.9409, -84.54818], zoom_start=12)

for latitudeInList, longitudeInList in zip(latitudeFromMapData, longitudeFromMapData):
    myMapFeatureGroup.add_child(folium.Marker(location=[latitudeInList, longitudeInList], popup='Volcano',icon=folium.Icon(color='blue')))

map.add_child(myMapFeatureGroup)
map.save('c:\\users\\trent\\desktop\\map\\map3.html')

