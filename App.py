import folium
import pandas as pd


html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

def color_producer(elevation):
    if elevation<1000:
        return 'orange'
    elif 1000<elevation<3000:
        return 'green'
    elif elevation>2000:
        return 'red'

#working on the volcano locations csv 
Vdf=pd.read_csv("Volcanoes.txt",sep=',')
V_coord=Vdf[["ELEV","NAME","LAT","LON"]]
lat=list(V_coord["LAT"])
lon=list(V_coord["LON"])
elev = list(V_coord["ELEV"])
name=list(V_coord["NAME"])


map=folium.Map(location=[39.56601396249721, -115.83795201489588],zoom_start=5.8,tiles = "Stamen Terrain")

fgv=folium.FeatureGroup(name="Volcanoes")

#adding the volcanoes info to the map
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fgv.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = color_producer(el))))
 
fgp=folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x : {'fillColor':'green' if x['properties']['POP2005']<10000000
 else 'orange' if 10000000<=x['properties']['POP2005']<20000000 else 'red' }))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")



