'''
import folium
import requests
import datetime

import os

def get_earthquake_data():
    url = 'https://earthquake.usgs.gov/fdsnws/event/1/query'
    parameters = {
        'format': 'geojson',
        'starttime': '2024-04-23',
        'endtime': '2024-04-25',
        'minmagnitude': '4.5',
        'orderby': 'time'
    }

    response = requests.get(url, params=parameters)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to fetch earthquake data")
        return None

# Get earthquake data
earthquake_data = get_earthquake_data()

# Create a map centered on a specific location
map_center = [0, 0]  # Change this to the desired location
map_center = [23.6978, 120.9605]
mymap = folium.Map(location=map_center, zoom_start=9)

# Plot earthquake data on the map
for quake in earthquake_data['features']:
    coordinates = quake['geometry']['coordinates'][:2]  # Extract lat and lon
    magnitude = quake['properties']['mag']
    title = quake['properties']['title']
    time = quake['properties']['time']
    
    # Convert time from milliseconds since epoch to a readable format
    time_str = datetime.datetime.fromtimestamp(time / 1000).strftime('%Y-%m-%d %H:%M:%S')

    popup_text = f"Magnitude: {magnitude}, Title: {title}, Time: {time_str}"

    
    folium.Marker(location=coordinates[::-1], popup=popup_text).add_to(mymap)

# Save the map as an HTML file
map_file = 'earthquake_map.html'
mymap.save(map_file)
#webbrowser.open('file://' + map_file)
os.system(f"open {map_file}")

'''


import folium
import requests
import datetime
import os

def get_earthquake_data():
    url = 'https://earthquake.usgs.gov/fdsnws/event/1/query'
    parameters = {
        'format': 'geojson',
        'starttime': '2024-04-23',
        'endtime': '2024-04-25',
        'minmagnitude': '4.5',
        'orderby': 'time'
    }

    response = requests.get(url, params=parameters)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to fetch earthquake data")
        return None

# Get earthquake data
earthquake_data = get_earthquake_data()

# Create a map centered on a specific location
#map_center = [0, 0]  # Change this to the desired location
map_center = [23.6978, 120.9605]
mymap = folium.Map(location=map_center, zoom_start=9)

# Plot earthquake data on the map
for idx, quake in enumerate(earthquake_data['features']):
    coordinates = quake['geometry']['coordinates'][:2]  # Extract lat and lon
    magnitude = quake['properties']['mag']
    title = quake['properties']['title']
    time = quake['properties']['time']
    
    # Convert time from milliseconds since epoch to a readable format
    time_str = datetime.datetime.fromtimestamp(time / 1000).strftime('%Y-%m-%d %H:%M:%S')

    popup_text = f"Magnitude: {magnitude}, Title: {title}, Time: {time_str}"
    
    # Set marker color to red for the last earthquake event
    if idx == 0: #len(earthquake_data['features']) - 1:
        folium.Marker(location=coordinates[::-1], popup=popup_text, icon=folium.Icon(color='red')).add_to(mymap)
    else:
        folium.Marker(location=coordinates[::-1], popup=popup_text).add_to(mymap)

# Save the map as an HTML file
map_file = 'earthquake_map.html'
mymap.save(map_file)

# Open the HTML file with the default program associated with HTML files
os.system(f"open {map_file}")
