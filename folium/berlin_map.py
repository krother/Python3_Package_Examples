import folium


berlin_map = folium.Map(location=[52.50, 13.35], zoom_start=13)

folium.Marker(
    (52.5157669, 13.3771557),
    popup="Brandenburger Tor",
    icon=folium.Icon(icon="map-marker", color="blue"),
).add_to(berlin_map)

folium.Marker(
    (52.5141987, 13.350284),
    popup="Siegessäule",
    icon=folium.Icon(icon="star", color="orange"),
).add_to(berlin_map)

folium.Marker(
    (52.4681216, 13.332078), popup="Home", icon=folium.Icon(icon="home", color="green")
).add_to(berlin_map)

berlin_map.save("berlin_map.html")

berlin_map  # in Jupyter to see the result
