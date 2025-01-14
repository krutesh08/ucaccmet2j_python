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


