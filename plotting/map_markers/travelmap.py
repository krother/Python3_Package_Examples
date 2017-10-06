"""
https://folium.readthedocs.io/en/latest/quickstart.html#markers

more icons see: http://getbootstrap.com/components/
"""

import folium
import pandas as pd

    
def draw_map_markers(filename, outfile, zoom):
    entries = pd.read_csv(filename, names=["lat", "long", "text", "icon", "color"], index_col=None)
    berlin_map = folium.Map(location=[52.50, 13.35], zoom_start=zoom)

    for i, row in entries.iterrows():
        coord = [row['lat'], row['long']]
        folium.Marker(coord, popup=row['text'],
            icon=folium.Icon(icon=row['icon'],
            color=row['color'])).add_to(berlin_map)

    berlin_map.save(outfile)


draw_map_markers('lectures_conferences.csv', 'map.html', 5)
