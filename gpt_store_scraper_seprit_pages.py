import requests
import json
import csv

base_url = "https://gptstore.ai/_next/data/U693FM1yXxTSYOQ9zSNbx/en/gpts.json?lang=all&page="

for page_num in range(1, 101):
    url = base_url + str(page_num)
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        page_props = data.get("pageProps", {})
        gpts = page_props.get("gpts", [])

        # Generate JSON file
        json_filename = f"gpt_store_data_page_{page_num}.json"
        with open(json_filename, "w", encoding="utf-8") as file:
            json.dump(gpts, file, indent=4, ensure_ascii=False)
        print(f"JSON data saved to {json_filename}")

        # Generate CSV file
        csv_filename = f"gpt_store_data_page_{page_num}.csv"
        with open(csv_filename, "w", newline='', encoding='utf-8') as csvfile:
            fieldnames = ['name', 'description', 'logo', 'gptId', 'gptUrl', 'conversionCount', 'authorName', 'pScore', 'beOut', 'customLink', 'star']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write the header row
            writer.writeheader()

            # Write the data rows
            for item in gpts:
                writer.writerow(item)

        print(f"CSV data saved to {csv_filename}")

    else:
        print(f"Request failed for page {page_num} with status code: {response.status_code}")
