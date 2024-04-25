import folium
import requests
import datetime
import os
from geopy.distance import geodesic


def get_earthquake_data():
    url = 'https://earthquake.usgs.gov/fdsnws/event/1/query'
    parameters = {
        'format': 'geojson',
        'starttime': '2024-04-23',
        'endtime': '2024-04-26',
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

def filter_earthquake_data(earthquake_data, reference_point, max_distance_km):
    filtered_data = []
    for quake in earthquake_data['features']:
        coordinates = quake['geometry']['coordinates'][:2]  # Extract lat and lon
        distance = geodesic(reference_point, coordinates[::-1]).kilometers
        if distance <= max_distance_km:
            filtered_data.append(quake)
    return filtered_data

# Get earthquake data
earthquake_data = get_earthquake_data()

# Reference point (e.g., center of Taiwan)
reference_point = (23.6978, 120.9605)
 
# Maximum distance in kilometers
max_distance_km = 100

# Filter earthquake data within 100km range
earthquake_data_filtered = filter_earthquake_data(earthquake_data, reference_point, max_distance_km)

# Create a map centered on the reference point
mymap = folium.Map(location=reference_point, zoom_start=9)

# Plot filtered earthquake data on the map
for idx, quake in enumerate(earthquake_data_filtered):
    coordinates = quake['geometry']['coordinates'][:2]  # Extract lat and lon
    magnitude = quake['properties']['mag']
    title = quake['properties']['title']
    time = quake['properties']['time']
    
    # Convert time from milliseconds since epoch to a readable format
    time_str = datetime.datetime.fromtimestamp(time / 1000).strftime('%Y-%m-%d %H:%M:%S')

    popup_text = f"Magnitude: {magnitude}, Title: {title}, Time: {time_str}"
    
    # Set marker color to red for the first earthquake event
    if idx == 0: #len(earthquake_data_filtered) - 1: #0:
        folium.Marker(location=coordinates[::-1], popup=popup_text, icon=folium.Icon(color='red')).add_to(mymap)
    else:
        folium.Marker(location=coordinates[::-1], popup=popup_text).add_to(mymap)



import pandas as pd
df = pd.DataFrame(earthquake_data_filtered)
#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
df['time'] = pd.to_datetime(df['properties'].apply(lambda x: x['time']), unit='ms').dt.strftime('%Y-%m-%d %H:%M:%S')

# Extract 'mag' and 'place' from 'properties'
df['mag'] = df['properties'].apply(lambda x: x['mag'])
df['place'] = df['properties'].apply(lambda x: x['place'])

# Display 'mag', 'place', and 'time' columns
print(df[['mag', 'place', 'time']])

# Save the map as an HTML file
map_file = 'earthquake_map.html'
mymap.save(map_file)

# Open the HTML file with the default program associated with HTML files
os.system(f"open {map_file}")

