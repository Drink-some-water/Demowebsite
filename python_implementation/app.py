from flask import Flask, render_template
from news_fetcher import fetch_news
import yake

app = Flask(__name__)

#news api key 31e52b26ece14e65a65c0ebfdf205032
API_KEY = '31e52b26ece14e65a65c0ebfdf205032'

def find_keywords(articles):
    #combine titles and descriptions
    text_for_keywords = " ".join([article["title"] + ". " + article["description"] for article in articles])
    #keyword extractor parameters
    kw_extractor = yake.KeywordExtractor(lan="en",  # english
                                            n=2,       # two word phrases
                                            dedupLim=0.3,  # strong deduplication
                                            top=5,    # top 5 keywords
                                            features=None)
   # Extract keywords
    return kw_extractor.extract_keywords(text_for_keywords)


def find_articles(keywords):
    articles = {}

    for keyword, _ in keywords:
        articles[keyword] = fetch_news(API_KEY, keyword)
    
    return articles


@app.route('/topic/<topic_name>')
def show_topic(topic_name):

    #first set of articles find keywords related to the topic
    initial_articles = fetch_news(API_KEY, topic_name)  
    top_keywords = find_keywords(initial_articles)

    #find and display articles based on keyword
    keyword_articles = find_articles(top_keywords)
    return render_template('topic.html', keyword_articles=keyword_articles)

@app.route('/')
def hello():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
