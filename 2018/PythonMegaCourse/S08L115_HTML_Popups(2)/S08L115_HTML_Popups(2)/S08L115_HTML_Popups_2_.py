import folium
import pandas
     
dataFromTxtFile = pandas.read_csv("d:\\users\\trent\\desktop\\new folder\\Volcanoes.txt")
lat = list(dataFromTxtFile["LAT"])
lon = list(dataFromTxtFile["LON"])
elev = list(dataFromTxtFile["ELEV"])
name = list(dataFromTxtFile["NAME"])

     
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""
     
map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name = "My Map")
     
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = "green")))
     
map.add_child(fg)
map.save("d:\\users\\trent\\desktop\\new folder\\Map_html_popup_advanced.html")
