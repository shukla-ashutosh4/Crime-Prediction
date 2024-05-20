# import gmplot

# # Set the center of the map to be the approximate center of Karnataka
# karnataka_center = (14.5204, 75.7224)  # Approximate latitude and longitude of Karnataka center

# # Initialize the map
# gmap = gmplot.GoogleMapPlotter(karnataka_center[0], karnataka_center[1], 8)  # Zoom level 8

# # Define the grid boundaries for Karnataka
# min_lat, max_lat = 11.5, 17.5  # Latitude boundaries
# min_lon, max_lon = 74.0, 78.5  # Longitude boundaries
# num_rows, num_cols = 10, 10  # Number of rows and columns for the grid

# # Calculate the latitude and longitude intervals for the grid
# lat_interval = (max_lat - min_lat) / num_rows
# lon_interval = (max_lon - min_lon) / num_cols

# # Generate grid coordinates
# grid_lats = [min_lat + i * lat_interval for i in range(num_rows + 1)]
# grid_lons = [min_lon + i * lon_interval for i in range(num_cols + 1)]

# # Plot grid lines
# for lat in grid_lats:
#     gmap.plot([lat] * (num_cols + 1), grid_lons, color='blue', edge_width=1)

# for lon in grid_lons:
#     gmap.plot(grid_lats, [lon] * (num_rows + 1), color='blue', edge_width=1)

# # Save the map to an HTML file
# gmap.draw("karnataka_map.html")






# import csv
# import random

# # Define the range of latitude and longitude for Bangalore
# bangalore_latitude_range = (12.8, 13.1)  # Example latitude range for Bangalore
# bangalore_longitude_range = (77.4, 77.8)  # Example longitude range for Bangalore

# # List of crimes
# crimes = ['Theft', 'Robbery', 'Assault', 'Burglary', 'Fraud', 'Vandalism', 'Kidnapping', 'Drug Offense', 'Arson', 'Homicide']

# # Generate 100 lines of data
# data = []
# for _ in range(100):
#     crime = random.choice(crimes)
#     latitude = round(random.uniform(*bangalore_latitude_range), 6)
#     longitude = round(random.uniform(*bangalore_longitude_range), 6)
#     data.append([crime, latitude, longitude])

# # Write data to CSV file
# with open('crime_data1.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Crime', 'Latitude', 'Longitude'])
#     writer.writerows(data)

# print("CSV file 'crime_data.csv' generated successfully.")

# # import pandas as pd
# # import folium
# # from folium.plugins import HeatMap
# # import time


# # import asyncio
# # from pyppeteer import launch

# # async def take_screenshot():
# #     browser = await launch()
# #     page = await browser.newPage()
# #     await page.setViewport({'width': 1920, 'height': 1080})  # Set viewport size as needed
# #     await page.goto("C:\\Program Files\\GitHub\\bangalore_map.html")  # Replace the path with the actual file path
# #     await page.waitForSelector('#graph-container')  # Wait for the map to load
# #     await browser.close()

# # # Run the asynchronous function
# # asyncio.get_event_loop().run_until_complete(take_screenshot())


# # # Load the anonymous data file (replace 'data.csv' with your file path)
# # data = pd.read_csv('crime_data.csv')

# # bangalore_map = ('bangalore_map.html')
# # for index, row in data.iterrows():
# #     folium.CircleMarker(
# #         location=[row['Latitude'], row['Longitude']],
# #         radius=5,
# #         fill=True,
# #         fill_color='red',
# #         color='red',
# #         fill_opacity=0.6
# #     ).add_to(bangalore_map)

# # # Generate heat map
# # heat_data = [[row['Latitude'], row['Longitude']] for index, row in data.iterrows()]
# # HeatMap(heat_data).add_to(bangalore_map)

# # async def take_screenshot():
# #     browser = await launch()
# #     page = await browser.newPage()
# #     await page.setViewport({'width': 1920, 'height': 1080})  # Set viewport size as needed
# #     await page.goto("C:\\Program Files\\GitHub\\bangalore_map.html")  # Replace the path with the actual file path
# #     await page.waitForSelector('#graph-container')  # Wait for the map to load
# #     await page.screenshot({'path': 'graph.png'})  # Take a screenshot and save it as 'graph.png'
# #     await browser.close()

# # # # Save the map as HTML
# # # bangalore_map.save("bangalore_map.html")

# # # # Specify the path to the Chrome WebDriver executable
# # # chrome_driver_path = "C:/path/to/chromedriver.exe"  # Replace with the actual path

# # # # Create a headless Chrome browser instance
# # # chrome_options = Options()
# # # chrome_options.add_argument("--headless")
# # # driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("D:\\Users\\Downloads\\South Crime Details.xlsx\\South Crime Details.csv", encoding='latin-1')

# Function to convert degrees, minutes, seconds format to decimal
def dms_to_decimal(dms):
    if isinstance(dms, float):
        return None
    
    try:
        components = dms.split('°')
        if len(components) < 2:
            return None
        
        degrees = components[0]
        rest = components[1]
        minutes = rest.split('\'')[0]
        seconds = rest.split('\'')[1].split('"')[0]
        direction = dms[-1]
        
        decimal = float(degrees) + float(minutes)/60 + float(seconds)/3600
        if direction in ['S', 'W']:
            decimal *= -1
        
        return decimal
    except (IndexError, ValueError):
        return None


# Convert latitude and longitude columns to decimal format
df['Latitude'] = df['Latitude'].apply(dms_to_decimal)
df['Longitude'] = df['Longitude'].apply(dms_to_decimal)

# Save the DataFrame with converted values back to a new CSV file
df.to_csv("converted_file.csv", index=False)
