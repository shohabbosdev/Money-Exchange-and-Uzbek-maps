import streamlit as st
import csv
import folium
from streamlit_folium import st_folium

datafile = 'uz.csv'

# Cache the data loading function
@st.cache_data
def read_data():
    data = []
    with open(datafile, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            latitude = float(row['lat'])
            longitude = float(row['lng'])
            data.append({
                'city': row['city'],
                'population': row['population'],
                'latitude': latitude,
                'longitude': longitude
            })
    return data

# Load the data
data = read_data()
CONNECTION_CENTER = (39.654397, 66.975836)
map = folium.Map(location=CONNECTION_CENTER, zoom_start=9)
sum=[]
for station in data:
    sum.append(station['population'])
    location = station['latitude'], station['longitude']
    folium.Marker(location, popup=station['city'], tooltip=station['population']).add_to(map)
summa=0
for i in range(51):
    summa+=int(sum[i])

st.write(f"Aholi soni {summa} ta ekan")
st.header("O'zbekiston xaritasi")
st_folium(map, use_container_width=True)
