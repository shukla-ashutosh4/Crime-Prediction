# # import pandas as pd
# # import matplotlib.pyplot as plt
# # import cartopy
# # import cartopy.crs as ccrs

# # # Read the crime data
# # data = pd.read_csv("C:\\Program Files\\GitHub\\crime_data1.csv")

# # # Create a new figure with Cartopy
# # plt.figure(figsize=(10, 8))
# # ax = plt.axes(projection=ccrs.PlateCarree())

# # # Plot the crime data as scatter points
# # ax.scatter(data['Longitude'], data['Latitude'], color='red', s=3, label='Crime Data')

# # # Add grid lines with dark color
# # gl = ax.gridlines(draw_labels=True)
# # gl.xlabel_style = {'color': 'black'}
# # gl.ylabel_style = {'color': 'black'}
# # gl.xlines = True
# # gl.ylines = True
# # gl.xformatter = cartopy.mpl.gridliner.LONGITUDE_FORMATTER
# # gl.yformatter = cartopy.mpl.gridliner.LATITUDE_FORMATTER
# # gl.xlabels_top = False
# # gl.ylabels_right = False
# # gl.xlocator = plt.MaxNLocator(5)
# # gl.ylocator = plt.MaxNLocator(5)
# # gl.grid_color = 'black'

# # # Set the map extent to Bangalore
# # ax.set_extent([77.3, 77.9, 12.7, 13.1])

# # # Add legend
# # plt.legend()

# # # Show the plot
# # plt.show()

# import pandas as pd
# import folium
# from folium.plugins import HeatMap, MeasureControl

# data = pd.read_csv("C:\\Program Files\\GitHub\\crime_data1.csv")

# # Define a custom tile layer with dark-colored grid lines
# custom_tile_layer = folium.TileLayer(
#     tiles='https://cartodb-basemaps-{s}.global.ssl.fastly.net/dark_all/{z}/{x}/{y}.png',
#     attr='© OpenStreetMap contributors, © CartoDB',
#     name='Custom Dark Tile Layer',
#     overlay=True,
#     control=True
# )

# # Create the map with the custom tile layer
# bangalore_map = folium.Map(
#     location=[12.9716, 77.5946],
#     zoom_start=12,
#     control_scale=True,
#     zoom_control=True
# )
# custom_tile_layer.add_to(bangalore_map)

# # Iterate over the rows in the data
# for _, row in data.iterrows():
#     latitude = row['Latitude']
#     longitude = row['Longitude']
#     # Check if latitude and longitude are not NaN
#     if not pd.isna(latitude) and not pd.isna(longitude):
#         # Add a CircleMarker for each valid coordinate
#         folium.CircleMarker(
#             location=[latitude, longitude],
#             radius=3,
#             fill=True,
#             fill_color='red',
#             color='red',
#             fill_opacity=0.6,
#             popup=f"Crime: {row['Crime']}, Latitude: {latitude}, Longitude: {longitude}"
#         ).add_to(bangalore_map)

# # Create a list of lists containing latitude and longitude pairs
# heat_data = [[row['Latitude'], row['Longitude']] for _, row in data.dropna(subset=['Latitude', 'Longitude']).iterrows()]

# # Remove NaN values from the heat data
# heat_data = [[lat, lon] for lat, lon in heat_data if not (pd.isna(lat) or pd.isna(lon))]

# # Add HeatMap layer to the map
# HeatMap(heat_data).add_to(bangalore_map)

# # Add MeasureControl to show gridlines and adjust scale based on zoom level
# measure_control = MeasureControl(primary_length_unit='meters')
# bangalore_map.add_child(measure_control)

# # Save the map as an HTML file
# bangalore_map.save("bangalore_crime_map.html")





import pandas as pd
import folium
from folium.plugins import HeatMap, MeasureControl

data = pd.read_csv("C:\\Program Files\\GitHub\\crime_data1.csv")

# Define a custom tile layer with dark background and light features
custom_tile_layer = folium.TileLayer(
    tiles='https://cartodb-basemaps-{s}.global.ssl.fastly.net/dark_all/{z}/{x}/{y}.png',
    attr='© OpenStreetMap contributors, © CartoDB',
    name='Custom Dark Tile Layer',
    overlay=True,
    control=True
)

# Create the map with the custom tile layer
bangalore_map = folium.Map(
    location=[12.9716, 77.5946],
    zoom_start=12,
    control_scale=True,
    zoom_control=True
)
custom_tile_layer.add_to(bangalore_map)

# Iterate over the rows in the data
for _, row in data.iterrows():
    latitude = row['Latitude']
    longitude = row['Longitude']
    # Check if latitude and longitude are not NaN
    if not pd.isna(latitude) and not pd.isna(longitude):
        # Add a CircleMarker for each valid coordinate
        folium.CircleMarker(
            location=[latitude, longitude],
            radius=3,
            fill=True,
            fill_color='red',
            color='red',
            fill_opacity=0.6,
            popup=f"Crime: {row['Crime']}, Latitude: {latitude}, Longitude: {longitude}"
        ).add_to(bangalore_map)

# Create a list of lists containing latitude and longitude pairs
heat_data = [[row['Latitude'], row['Longitude']] for _, row in data.dropna(subset=['Latitude', 'Longitude']).iterrows()]

# Remove NaN values from the heat data
heat_data = [[lat, lon] for lat, lon in heat_data if not (pd.isna(lat) or pd.isna(lon))]

# Add HeatMap layer to the map
HeatMap(heat_data).add_to(bangalore_map)

# Add MeasureControl to show gridlines and adjust scale based on zoom level
measure_control = MeasureControl(primary_length_unit='meters')
bangalore_map.add_child(measure_control)

# Save the map as an HTML file
bangalore_map
