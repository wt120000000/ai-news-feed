import requests
import json

API_KEY = "0600a4a2958f99c9c27974d102ec9d3e"
query = "artificial intelligence"
url = f"https://gnews.io/api/v4/search?q={query}&lang=en&token={API_KEY}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    # Print each article
    for article in data['articles']:
        print(f"Title: {article['title']}")
        print(f"Source: {article['source']['name']}")
        print(f"URL: {article['url']}")
        print("----")

    # Save articles to JSON file
    with open("ai_news.json", "w", encoding="utf-8") as f:
        json.dump(data['articles'], f, ensure_ascii=False, indent=4)

else:
    print("Error:", response.status_code, response.text)
