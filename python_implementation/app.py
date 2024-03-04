from flask import Flask, render_template
from news_fetcher import fetch_news
import yake

app = Flask(__name__)

#news api key 31e52b26ece14e65a65c0ebfdf205032
API_KEY = '31e52b26ece14e65a65c0ebfdf205032'

def extract_topics(articles):
    #join titles with description text
    text = " ".join([article["title"] + ". " + article["description"] for article in articles])
    kw_extractor = yake.KeywordExtractor(lan="en",  # Language
                                            n=2,       # Max n-gram size
                                            dedupLim=0.3,  # Deduplication threshold
                                            top=100,    # Number of keywords to extract
                                            features=None)
    # Extract keywords
    keywords = kw_extractor.extract_keywords(text)
    for kw, score in keywords:
        print(kw, score)


@app.route('/topic/<topic_name>')
def show_topic(topic_name):
    articles = fetch_news(API_KEY, topic_name)
    #extract_topics(articles)
    return render_template('topic.html', articles=articles, topic=topic_name)

@app.route('/')
def hello():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
