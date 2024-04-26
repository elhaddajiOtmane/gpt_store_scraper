import requests
from bs4 import BeautifulSoup
import json

# Function to extract GPT data from a single page
def extract_gpt_data(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    gpt_data = []
    gpt_cards = soup.select('a.gpt-card')

    for card in gpt_cards:
        name = card.select_one('h3.gpt-name').text.strip()
        description = card.select_one('p.gpt-description').text.strip()
        logo = card.select_one('img.gpt-logo')['src']
        gpt_id = card.get('href').split('/')[-1]
        gpt_url = f"https://gptstore.ai/{card.get('href')}"
        conversion_count = card.select_one('span.conversion-count')
        if conversion_count:
            conversion_count = int(conversion_count.text.strip().replace(',', ''))
        else:
            conversion_count = None
        author_name = card.select_one('span.gpt-author').text.strip()
        p_score = card.select_one('span.p-score')
        if p_score:
            p_score = float(p_score.text.strip())
        else:
            p_score = None
        star_rating = card.select_one('span.star-rating')
        if star_rating:
            star_rating = float(star_rating.text.strip())
        else:
            star_rating = None

        gpt_data.append({
            'name': name,
            'description': description,
            'logo': logo,
            'gptId': gpt_id,
            'gptUrl': gpt_url,
            'conversionCount': conversion_count,
            'authorName': author_name,
            'pScore': p_score,
            'star': star_rating
        })

    return gpt_data

# Main function to scrape data from pages 1 to 100
def scrape_gpt_store():
    all_gpt_data = []

    for page_num in range(1, 101):
        page_url = f"https://gptstore.ai/_next/data/U693FM1yXxTSYOQ9zSNbx/en/gpts.json?lang=all&page={page_num}"
        page_data = extract_gpt_data(page_url)
        all_gpt_data.extend(page_data)

    return all_gpt_data

# Call the main function and save the data to a JSON file
gpt_data = scrape_gpt_store()
with open('gpt_store_data.json', 'w', encoding='utf-8') as f:
    json.dump(gpt_data, f, ensure_ascii=False, indent=2)
