import json

seattle_station_code = "GHCND:US1WAKG0038"  

# Load the precipitation data
with open('ucaccmet2j_python/precipitation.json', 'r') as file:
    precipitation_data = json.load(file)

# Filter data for Seattle
seattle_data = []
for entry in precipitation_data:
    if entry['station'] == seattle_station_code:
        seattle_data.append(entry)

# Initializing the dictionary with months as keys
monthly_precipitation = {
    "01": 0, "02": 0, "03": 0, "04": 0,
    "05": 0, "06": 0, "07": 0, "08": 0,
    "09": 0, "10": 0, "11": 0, "12": 0
}
for entry in seattle_data:
    date = entry['date']  
    month = date.split('-')[1]  # Extract the month (e.g., "01" for January)
    if month not in monthly_precipitation:
        monthly_precipitation[month] = 0
    monthly_precipitation[month] += entry['value']  # Sum precipitation (in tenths of mm)

# Convert precipitation values to mm (from tenths of mm)
for month in monthly_precipitation:
    monthly_precipitation[month] = monthly_precipitation[month] / 10

# Save results to results.json
results = {
    "Seattle": {
        "station": seattle_station_code,
        "state": "WA",
        "total_monthly_precipitation": monthly_precipitation
    }
}

with open('results.json', 'w') as file:
    json.dump(results, file, indent=4)


# Part 2 

# Extract Seattle's monthly precipitation data
monthly_precipitation = results["Seattle"]["total_monthly_precipitation"]

total_yearly_precipitation = sum(monthly_precipitation.values())

relative_monthly_precipitation = {}
# Loop through each month in the monthly_precipitation dictionary
for month in monthly_precipitation:
    # Get the precipitation value for the current month
    value = monthly_precipitation[month]
    
    # Calculate the relative precipitation for the month
    relative_value = value / total_yearly_precipitation
    
    # Add the result to the relative_monthly_precipitation dictionary
    relative_monthly_precipitation[month] = relative_value

results["Seattle"]["total_yearly_precipitation"] = total_yearly_precipitation
results["Seattle"]["relative_monthly_precipitation"] = relative_monthly_precipitation   

with open('results.json', 'w') as file:
    json.dump(results, file, indent=4)

# Part 3 - INCOMPLETE

import csv

with open('ucaccmet2j_python/stations.csv', 'r') as file:
    stations = list(csv.DictReader(file))  