# import pandas as pd

# # Read the Excel file
# df = pd.read_csv("C:\\Program Files\\GitHub\\KSP\\Cleaned_data.csv")

# # Clear rows where both latitude and longitude are zero
# df = df[(df['Latitude'] != 0) | (df['Longitude'] != 0)]

# # Write back to Excel
# df.to_excel('your_file.xlsx', index=False)

# import pandas as pd

# # Read the Excel file
# file_path = "C:\\Program Files\\GitHub\\KSP\\Cleaned_data.csv"
# data = pd.read_csv(file_path, encoding='latin1')

# # Filter rows containing "Bengaluru" in any column
# bengaluru_data = data[data.apply(lambda row: row.astype(str).str.contains('Bengaluru', case=False).any(), axis=1)]

# # Save the filtered data to a new CSV file
# output_file_path = "C:\\Program Files\\GitHub\\KSP\\bengaluru_data.csv"
# bengaluru_data.to_csv(output_file_path, index=False)

# # Print the path of the new CSV file
# print("Filtered data saved to:", output_file_path)


import pandas as pd

# Read the CSV file
file_path = "C:\\Program Files\\GitHub\\KSP\\crime_data1.csv"
data = pd.read_csv(file_path, usecols=['Latitude', 'Longitude'], encoding='latin1')

# Drop rows with missing values
data.dropna(inplace=True)

# Round latitude and longitude values to 3 decimal places
data['Latitude'] = data['Latitude'].round(3)
data['Longitude'] = data['Longitude'].round(3)

# Remove duplicate locations
data.drop_duplicates(inplace=True)

# Save the filtered data to a new CSV file
output_file_path = "C:\\Program Files\\GitHub\\KSP\\crime_data1.csv"
data.to_csv(output_file_path, index=False)

# Print the path of the new CSV file
print("Filtered data saved to:", output_file_path)





