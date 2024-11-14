import pandas as pd
import folium
from folium.plugins import MarkerCluster

df = pd.read_csv('./python/cleaned_meteor.csv')

m = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=12)

marker_cluster = MarkerCluster().add_to(m)

for index, row in df.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']], 
                  popup=f"{row['Class']} - {row['Year']} - {row['Mass']}",
                  tooltip=row['Meteor Name']).add_to(marker_cluster)

m.save('map.html')

m
