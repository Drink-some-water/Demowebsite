#see full list of available parameters at bottom of file. Message Sean Collins for api key or set up your own. 
#Further instructions in main function


import worldnewsapi
from pprint import pprint
import os
from datetime import datetime, timedelta


def get_earliest_publish_date():
    now = datetime.now()
    # Subtract 24 hours from the current datetime
    twenty_four_hours_ago = now - timedelta(hours=24)
    earliest_publish_date = twenty_four_hours_ago.strftime('%Y-%m-%d %H:%M:%S')
    return earliest_publish_date


def default_fetch_news():
    params = {
        'text': 'politics',
        'source_countries': 'us',
        'language': 'en',
        'earliest_publish_date': get_earliest_publish_date(),
        'number': 100
    }
    return fetch_news(params)


def fetch_news(api_params):
    configuration = worldnewsapi.Configuration()
    #below are different ways to include API key, see https://github.com/ddsky/world-news-api-clients/blob/main/python/docs/NewsApi.md#search_news
    configuration.api_key['apiKey'] = os.environ["API_KEY"]
    #configuration.api_key['headerApiKey'] = os.environ["API_KEY"]
    with worldnewsapi.ApiClient(configuration) as api_client:
        api_instance = worldnewsapi.NewsApi(api_client)
        try:
            api_response = api_instance.search_news(**api_params)
            return api_response
        except Exception as e:
            print(f"Exception when calling NewsApi->search_news: {e}\n")


if __name__ == '__main__':
    #set env variable permanently in cmd. Replace "api key" with your own in quotes
    #setx API_KEY "api key"
    params = {
        'text': 'politics',
        'source_countries': 'us',
        'language': 'en',
        'number': 5
    }
    pprint(fetch_news(params))


# EXAMPLES OF ALL POSSIBLE ARGUMENTS FOR API CALL
#    text = 'hurricane' # str | The text to match in the news content. (optional)
#    source_countries = 'us,uk' # str | A comma-separated list of ISO 3166 country codes from which the news should originate, e.g. gb,us. (optional)
#    language = 'en' # str | The ISO 6391 language code of the news, e.g. \"en\" for English. (optional)
#    min_sentiment = -0.8 # float | The minimal sentiment of the news in range [-1,1]. (optional)
#    max_sentiment = 0.8 # float | The maximal sentiment of the news in range [-1,1]. (optional)
#    earliest_publish_date = '2022-04-22 16:12:35' # str | The news must have been published after this date. (optional)
#    latest_publish_date = '2022-05-23 24:16:27' # str | The news must have been published before this date. (optional)
#    news_sources = 'https://www.bbc.co.uk' # str | A comma-separated list of news sources from which the news should originate, e.g. https://www.bbc.co.uk (optional)
#    authors = 'John Doe' # str | A comma-separated list of author names. Only news from any of the given authors will be returned. (optional)
#    entities = 'ORG:Tesla' # str | Filter news by entities, e.g. ORG:Tesla. (optional)
#    location_filter = '51.050407,13.737262,100' # str | Filter news by radius around a certain location. Format is \"latitude,longitude,radius in kilometers\", e.g. 51.050407, 13.737262, 100 (optional)
#    offset = 10 # int | The number of news to skip in range [0,1000] (optional)
#    number = 1 # int | The number of news to return in range [1,100] (optional)
#    sort = 'publish-time' # str | The sorting criteria. (optional)
#    sort_direction = 'desc' # str | Whether to sort ascending or descending. (optional)