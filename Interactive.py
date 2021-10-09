import folium
from folium.map import Icon
import pandas


#############USE API##############


data = pandas.read_csv("US-Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%s%%22" target="_blank">%s%s</a><br>
Height: %s m
"""


def colour_producer(elevation):
    if elevation < 1000:
        return "lightgreen"
    elif 1000 <= elevation < 2000:
        return "green"
    elif 2000 <= elevation < 3000:
        return "orange"
    elif 3000 <= elevation < 4000:
        return "red"
    else:
        return "darkred"


map = folium.Map(location=[38.58, -99.09],
                 zoom_start=6, tiles="Stamen Terrain")
fgv = folium.FeatureGroup(name="US Volcanoes")


for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (
        name, " Volcano", name, " Volcano", el), width=150, height=90)

    fgv.add_child(folium.CircleMarker(
        location=[lt, ln], radius=6, popup=folium.Popup(iframe), color='grey', fill=True, fill_color=colour_producer(el), fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")


fgp.add_child(folium.GeoJson(
    data=open('world.json', 'r', encoding='utf-8-sig').read(),
    style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                              else 'yellow' if 10000000 <= x['properties']['POP2005'] < 20000000
                              else 'orange' if 20000000 <= x['properties']['POP2005'] < 30000000
                              else 'red' if 30000000 <= x['properties']['POP2005'] < 40000000
                              else 'darkred'}))


map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())
map.save("Map1.html")


# print(map)

# print(dir(folium))

# print(help(folium.vector_layers.path_options))

# print(help(folium.Map))

# print(help(folium.add_child))

# print(data)

# icon=folium.Icon(color=colour_producer(el))))

#####################################################################
