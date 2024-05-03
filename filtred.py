import json

# Open the file with UTF-8 encoding
with open('csvjson.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Iterate over each item in the JSON data
for item in data:
    # Remove the "GPT Capabilities Actions Details" key if it exists
    if "GPT Capabilities Actions Details" in item:
        del item["GPT Capabilities Actions Details"]

# Save the modified JSON data back to the file
with open('csvjson.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)