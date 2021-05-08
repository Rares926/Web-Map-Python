import folium
import pandas as pd

print(dir(folium))
# print(help(folium.Marker))


# fg.add_child(folium.CircleMarker(location=[lt, ln], popup=folium.Popup(iframe),radius=10,fill_color=color_producer(el),color='grey',fill_opacity=0.7 ))



html_S = """<h4>Starbucks Info:</h4>
StoreNumber: %s 
"""


#working on the starbucks location csv  
# Sb=pd.read_csv("stores.csv",sep=',')
# Sb=Sb.dropna()
# Sb_info=Sb[["StoreNumber","Longitude","Latitude"]]
# Slat=list(Sb_info["Latitude"])
# Slon=list(Sb_info["Longitude"])
# SsN=list(Sb_info["StoreNumber"])

Starbucks=folium.FeatureGroup(name="Starbucks")


 #adding starbucks info to the map 
# for lt,ln,Sn in zip(Slat,Slon,SsN):
#     iframe = folium.IFrame(html=html_S % Sn, width=250, height=100)
#     Starbucks.add_child(folium.Marker(location=[lt,ln],popup=folium.Popup(iframe),icon=folium.Icon(color='blue')))

map.add_child(Starbucks)