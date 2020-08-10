import folium
import pandas


map=folium.Map(location=[13.749760,100.492262],zoom_start=10,tiles="Stamen Terrain")

data=pandas.read_csv("https://raw.githubusercontent.com/meawpantasia/urban-farm-thailand/master/MELON%20LIST%20MAP.csv")

na=list(data["Name"])
lat=list(data["LAT"])
lon=list(data["LON"])

fg=folium.FeatureGroup(name="melon farm")

for na,lat,lon in zip(na,lat,lon):
     fg.add_child(folium.CircleMarker(
    location=[lat,lon],
    radius=5,
    fill=False,
    fill_color='#00008B',
    color='#00008B',
    popup=na))

map.add_child(fg)


map.save("proud.html")