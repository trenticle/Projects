import cv2
import numpy
import jupyter
import folium
import pandas

# Ex1 open and print txt file
volcanoesFile = open('c:\\users\\trent\\desktop\\map\\volcanoes.txt')
volcanoesText = volcanoesFile.read()
volcanoesFile.close()
print(volcanoesText)

# Ex2 use pandas to work with txt
data = pandas.read_csv('c:\\users\\trent\\desktop\\map\\volcanoes.txt')


myMap = folium.Map(zoom_start= [12], location= [33.952602, -84.549934])
featureGroup = folium.FeatureGroup(name= 'My Map')
featureGroup.add_child(folium.Marker(location= [33.940907, -84.548187], popup='Home', icon= folium.Icon(color= 'green')))
myMap.add_child(featureGroup)
myMap.save ('c:\\users\\trent\\desktop\\map\\map2.html')
