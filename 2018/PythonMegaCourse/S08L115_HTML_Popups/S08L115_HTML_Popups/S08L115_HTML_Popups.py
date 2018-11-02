import folium
import pandas
     
data = pandas.read_csv('d:\\users\\trent\\desktop\\new folder\\Volcanoes.txt')
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'yellow'
    else:
        return 'orange'
          
map = folium.Map(location=[33.9409, -84.54818], zoom_start=12 )
fg = folium.FeatureGroup(name = "My Map")
     
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el)+ ' m', icon= folium.Icon(color= color_producer(el))))
     
     
map.add_child(fg)
map.save('d:\\users\\trent\\desktop\\new folder\\Map6.html')
