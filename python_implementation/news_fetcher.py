import requests


def fetch_news(api_key, topic):
    base_url = "https://newsapi.org/v2/everything"
    params = {
        'q': topic,
        'apiKey': api_key,
        'language': 'en',
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        articles_data = response.json().get('articles', [])
        articles = []
        for article in articles_data:
            articles.append({
                'title': article['title'],
                'description': article['description'],
                'url': article['url'],
                'imageUrl': article.get('urlToImage')  # Extracting the image URL
            })
        return articles
    else:
        return []

