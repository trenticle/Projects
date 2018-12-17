import cv2
import numpy
import jupyter
import folium

# example 1
myMap = folium.Map(zoom_start= [12], location= [33.952602, -84.549934])
featureGroup = folium.FeatureGroup(name= 'My Map')
featureGroup.add_child(folium.Marker(location= [33.940907, -84.548187], popup='Home', icon= folium.Icon(color= 'green')))
myMap.add_child(featureGroup)
myMap.save ('c:\\users\\trent\\desktop\\map\\map2.html')

# example 2 using a for loop to add coordinates NOTE: same "name" for each marker
myMap = folium.Map(zoom_start= [12], location= [33.952602, -84.549934])
featureGroup = folium.FeatureGroup(name= 'My Map')
for coordinates in [[33.940907, -84.548187],[33.93, -84.44]]:
    featureGroup.add_child(folium.Marker(location= coordinates, popup='Home', icon= folium.Icon(color= 'green')))
myMap.add_child(featureGroup)
myMap.save ('c:\\users\\trent\\desktop\\map\\map2.html')