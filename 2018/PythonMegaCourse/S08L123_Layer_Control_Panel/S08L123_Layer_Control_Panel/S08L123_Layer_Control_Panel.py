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
fgv = folium.FeatureGroup(name = "Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius= None , popup=str(el)+ ' m', fill_color= color_producer(el), color= 'black', fill= True, fill_opacity= .9))

fgp = folium.FeatureGroup(name = "Population")

fgp.add_child(folium.GeoJson(data= open('C:\\Users\\trent\\Desktop\\map\\world.json', 'r', encoding='utf-8-sig').read(), style_function= lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save('c:\\users\\trent\\desktop\\map\\Map11.html')




