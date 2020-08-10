import folium
import pandas 



m=folium.Map(location=[13.807264, 100.616063],zoom_start=10,tiles='Stamen Terrain')


data=pandas.read_csv("https://github.com/meawpantasia/urban-farm-thailand/blob/master/MELON%20LIST.csv")

n=list(data["PROVINCE"])
lat=list(data["LAT"])
lon=list(data["LON"])

fg=folium.FeatureGroup(name="Urban farm map")

for n,lat,lon in zip(n,lat,lon):
    fg.add_child(folium.CircleMarker(
    location=[lat,lon],
    radius=8,
    fill=False,
    fill_color='#00008B',
    color='#00008B',
    popup=n))

m.add_child(fg)




m.save("mapping.html")
