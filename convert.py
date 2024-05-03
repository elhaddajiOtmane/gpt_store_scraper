import json
import csv

# Open the JSON file
with open('csvjson.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Open a new CSV file for writing
with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = list(data[0].keys())  # Get the keys from the first item as column names
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()  # Write the column names as the header row

    for item in data:
        writer.writerow(item)  # Write each item as a row in the CSV file