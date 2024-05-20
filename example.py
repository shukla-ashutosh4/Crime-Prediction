# import pandas as pd
# import folium
# from folium.plugins import HeatMap, MeasureControl
# import numpy as np
# import geopy
# from geopy.geocoders import Nominatim
# import openpyxl

# # Read the crime data from CSV file
# data = pd.read_csv("C:\\Program Files\\GitHub\\KSP\\crime_data1.csv")

# # Filter out rows with missing latitude or longitude values
# filtered_data = data.dropna(subset=['Latitude', 'Longitude'])

# # Create a Folium map centered around Bangalore
# bangalore_map = folium.Map(location=[12.9716, 77.5946], zoom_start=12)

# # Create a feature group for gridlines
# grid_lines = folium.FeatureGroup(name='Gridlines', overlay=True, control=False)

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

# # Create a list of lists containing latitude and longitude pairs for HeatMap
# heat_data = [[row['Latitude'], row['Longitude']] for _, row in filtered_data.iterrows()]

# # Remove NaN values from the heat data
# heat_data = [[lat, lon] for lat, lon in heat_data if not (pd.isna(lat) or pd.isna(lon))]

# # Add HeatMap layer to the map
# HeatMap(heat_data).add_to(bangalore_map)

# # Calculate bounding box of data
# min_lat, max_lat = min(data['Latitude']), max(data['Latitude'])
# min_lon, max_lon = min(data['Longitude']), max(data['Longitude'])

# # Calculate grid spacing based on data range
# lat_range = max_lat - min_lat
# lon_range = max_lon - min_lon
# grid_spacing = min(lat_range, lon_range) / 20  # Adjust the denominator for gridline density

# # Add the gridlines
# for lat in np.arange(min_lat, max_lat, grid_spacing):
#     folium.PolyLine([(lat, min_lon), (lat, max_lon)], color='black', weight=1).add_to(bangalore_map)

# for lon in np.arange(min_lon, max_lon, grid_spacing):
#     folium.PolyLine([(min_lat, lon), (max_lat, lon)], color='black', weight=1).add_to(bangalore_map)

# # Add extra lines to fully close the grid
# folium.PolyLine([(min_lat, min_lon), (max_lat, min_lon)], color='black', weight=1).add_to(bangalore_map)
# folium.PolyLine([(max_lat, min_lon), (max_lat, max_lon)], color='black', weight=1).add_to(bangalore_map)
# folium.PolyLine([(max_lat, max_lon), (min_lat, max_lon)], color='black', weight=1).add_to(bangalore_map)
# folium.PolyLine([(min_lat, max_lon), (min_lat, min_lon)], color='black', weight=1).add_to(bangalore_map)

# # Add MeasureControl to show gridlines and adjust scale based on zoom level
# measure_control = MeasureControl(primary_length_unit='centimeters')
# bangalore_map.add_child(measure_control)

# # Add a JavaScript callback function to handle map clicks
# bangalore_map.get_root().html.add_child(folium.Element(
#     """
#     <script>
#         function onMapClick(e) {
#             var lat = e.latlng.lat.toFixed(6);
#             var lon = e.latlng.lng.toFixed(6);
#             var address = '';
#             fetch('https://nominatim.openstreetmap.org/reverse?format=json&lat=' + lat + '&lon=' + lon)
#                 .then(response => response.json())
#                 .then(data => {
#                     address = data.display_name;
#                     var proceed = confirm('Selected location: Latitude: ' + lat + ', Longitude: ' + lon + ', Address: ' + address + '. Proceed?');
#                     if (proceed) {
#                         var xhr = new XMLHttpRequest();
#                         xhr.open('POST', 'save_location', true);
#                         xhr.setRequestHeader('Content-Type', 'application/json');
#                         xhr.send(JSON.stringify({lat: lat, lon: lon, address: address}));
#                     }
#                 });
#         }
#         map.on('click', onMapClick);
#     </script>
#     """
# ))

# # Display the map
# bangalore_map



# from matplotlib import pyplot as plt  
# import numpy as np
# import math 

# def manhattan(A, B):
#     return abs(A[0] - B[0]) + abs(A[1] - B[1])

# def nearest(A, L):
#     n = len(L)
#     m = A
#     d = 0
#     p = 0
#     j = 0
#     while True:
#       if A[0] != L[j][0] or A[1] != L[j][1]:
#         #m = L[j]
#         d = manhattan(A,L[j])
#         p = j
#         break 
#       else: j += 1
#     for i in range(len(L)):
#       dis = manhattan(A,L[i])
#       if dis != 0 and dis < d:
#         d = dis
#         p = i
#     return L[p]

# def radius_buffer(L):
#     s = 0
#     n = len(L)
#     for i in range(n):
#       M = L.copy()
#       del M[i]
#       B = nearest(L[i], M)
#       s += manhattan(L[i],B)
#     return s/(2*n)

# def proba(i, j, L):  
#     # gives proba of criminal living in (i,j)
#     # L = list of crime sites   (n,2) list
#     proba = 0
#     f = 1/3
#     g = 2/3
#     B = radius_buffer(L)
#     for p in range(len(L)):
#       d = manhattan(L[p], [i,j])
#       if d > B:
#         proba += 1/(d**f)
#       else:
#         proba += B**(g-f)/((2*B - d)**g)
#     return proba

# def matriix_proba(m,n,L):
#   M = [[0 for j in range(n)] for i in range(m)]
#   for i in range(m):
#     for j in range(n):
#       M[i][j] += proba(i,j,L)
#   return M

# def draw_proba_grid(L,A, m, n):
#     proba_matrix = matriix_proba(m,n,L)
#     fig = plt.figure(dpi=200)
#     img = plt.imshow(proba_matrix, interpolation='nearest', origin='lower')
#     plt.scatter(A[1], A[0], color="r", label='Williams Residence', s = 3)
#     plt.scatter([a[1] for a in L], [a[0] for a in L], color="w", label ='Crime Site', s = 3)
#     plt.legend(numpoints=1)
#     plt.show()

# # Sample usage:
# crime_locations = [[12.9716, 77.5946], [12.9719, 77.5951], [12.9725, 77.5932], [12.9708, 77.5939], [12.9732, 77.5945]]
# williams_residence = [12.9720, 77.5940]
# draw_proba_grid(crime_locations, williams_residence, 100, 100)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def manhattan_distance(A, B):
    return abs(A[0] - B[0]) + abs(A[1] - B[1])

def nearest_neighbor(A, L):
    n = len(L)
    m = A
    d = 0
    p = 0
    j = 0
    while True:
        if A[0] != L[j][0] or A[1] != L[j][1]:
            d = manhattan_distance(A, L[j])
            p = j
            break
        else:
            j += 1
    for i in range(len(L)):
        dis = manhattan_distance(A, L[i])
        if dis != 0 and dis < d:
            d = dis
            p = i
    return L[p]

def radius_buffer(L):
    s = 0
    n = len(L)
    for i in range(n):
        M = L.copy()
        del M[i]
        B = nearest_neighbor(L[i], M)
        s += manhattan_distance(L[i], B)
    return s / (2 * n)

def probability(i, j, L):
    proba = 0
    f = 1 / 3
    g = 2 / 3
    B = radius_buffer(L)
    for p in range(len(L)):
        d = manhattan_distance(L[p], [i, j])
        if d > B:
            proba += 1 / (d ** f)
        else:
            proba += B ** (g - f) / ((2 * B - d) ** g)
    return proba

def probability_matrix(m, n, L):
    M = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            M[i][j] += probability(i, j, L)
    return M

def plot_proba_grid(crime_csv, residence_lat, residence_lon, m, n):
    # Read crime locations from CSV file
    crime_df = pd.read_csv(crime_csv)
    crime_locations = crime_df[['Latitude', 'Longitude']].values.tolist()

    # Calculate the probability matrix
    proba_matrix = probability_matrix(m, n, crime_locations)

    # Plotting
    fig = plt.figure(dpi=200)
    img = plt.imshow(proba_matrix, interpolation='nearest', origin='lower')
    plt.scatter(residence_lon, residence_lat, color="r", label='Residence of Williams', s=3)
    plt.scatter([a[1] for a in crime_locations], [a[0] for a in crime_locations], color="w", label='Crime Site', s=3)
    plt.legend(numpoints=1)
    plt.show()

# Sample usage:
crime_csv_path = "crime_data1.csv"  # Provide the path to your CSV file containing Crime, Latitude, and Longitude
residence_lat = 12.818605
residence_lon = 77.78713800000014
plot_proba_grid(crime_csv_path, residence_lat, residence_lon, 100, 100)


