# from faker import Faker
# import random
# import csv

# # Initialize Faker to generate fake data
# fake = Faker()

# # Create a list of police stations in Bangalore
# police_stations = ["Police Station A", "Police Station B", "Police Station C", "Police Station D", "Police Station E"]

# # Function to generate random crime data
# def generate_crime_data():
#     year = random.randint(2010, 2023)
#     crime_type = random.choice(["Robbery", "Assault", "Burglary", "Theft", "Fraud"])
#     date = fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d')
#     time = fake.time(pattern="%H:%M:%S")
#     place = fake.street_address()
#     latitude = fake.latitude()
#     longitude = fake.longitude()
#     criminal_name = fake.name()
#     criminal_latitude = fake.latitude()
#     criminal_longitude = fake.longitude()
#     criminal_age = random.randint(18, 70)
#     criminal_sex = random.choice(["Male", "Female"])
#     police_station = random.choice(police_stations)
    
#     return [police_station, year, crime_type, date, time, place, latitude, longitude, criminal_name, criminal_latitude, criminal_longitude, criminal_age, criminal_sex]

# # Generate 10000 lines of crime data
# crime_data = [generate_crime_data() for _ in range(10000)]

# # Write the data to a CSV file
# with open('crime_data_bangalore.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Police Station", "Year", "Type", "Date", "Time", "Place", "Latitude_of_crime", "Longitude_of_crime", "Name_of_criminal", "Latitude_of_criminal_home", "Longitude_of_criminal_home", "Age_of_criminal", "Sex_of_criminal"])
#     writer.writerows(crime_data)


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

# Step 1: Data Preparation
crime_data = pd.read_csv("D:\\Users\\Downloads\\FIR_Details_Data.csv", low_memory=False)

# Step 2: Feature Engineering
X = crime_data[['CrimeHead_Name', 'Latitude', 'Longitude']]
y = crime_data['Year']  # Change the target column to an existing one in your dataset

# Additional features: Distance from each location to past crime locations
def calculate_distance(x, y, past_crimes):
    return np.sqrt((x - past_crimes['Latitude'])**2 + (y - past_crimes['Longitude'])**2)

for i in range(len(crime_data)):
    X[f'Distance_to_Crime_{i}'] = calculate_distance(X['Latitude'], X['Longitude'], crime_data.iloc[:i])

# Step 3: Data Splitting
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 5: Model Training
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Step 6: Model Evaluation
y_pred = model.predict(X_test_scaled)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")


# Step 7: Predictions
# Replace new_lat1, new_lat2, etc. with actual latitude values for new locations
# new_locations = pd.DataFrame({'Latitude': [16.003307, 10.003307], 'Longitude': [82.369636, 79.3696362]})
# new_locations_scaled = scaler.transform(new_locations)
# predictions = model.predict(new_locations_scaled)
