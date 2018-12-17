import folium
import pandas

data = pandas.read_csv('c:\\users\\trent\\desktop\\map\\Volcanoes.txt')
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
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius= None , popup=str(el)+ ' m', fill_color= color_producer(el), color= 'black', fill= True, fill_opacity= .9))

fg.add_child(folium.GeoJson(data=(open('C:\\Users\\trent\\Desktop\\map\\world.json', 'r', encoding='utf-8-sig').read())))


map.add_child(fg)
map.save('c:\\users\\trent\\desktop\\map\\Map8.html')


