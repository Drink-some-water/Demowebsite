from rest_framework.views import APIView
from rest_framework.response import Response
import os
from datetime import datetime, timedelta
import worldnewsapi


class WorldNewsAPIInterface(APIView):

    def get_earliest_publish_date(self):
        now = datetime.now()
        twenty_four_hours_ago = now - timedelta(hours=24)
        return twenty_four_hours_ago.strftime('%Y-%m-%d %H:%M:%S')

    def fetch_news(self, api_params):
        configuration = worldnewsapi.Configuration()
        configuration.api_key['apiKey'] = os.environ.get("API_KEY", "")
        with worldnewsapi.ApiClient(configuration) as api_client:
            api_instance = worldnewsapi.NewsApi(api_client)
            try:
                api_response = api_instance.search_news(**api_params)
                return api_response
            except Exception as e:
                print(f"Exception when calling NewsApi->search_news: {e}")
                return {}

    def get(self, request, *args, **kwargs):
        #set default parameters. Overridden by any query params that are passed
        api_params = {
            'text': request.query_params.get('text', 'politics'),
            'source_countries': request.query_params.get('source_countries', 'us'),
            'language': request.query_params.get('language', 'en'),
            'earliest_publish_date': request.query_params.get('earliest_publish_date', self.get_earliest_publish_date()),
            'number': request.query_params.get('number', '100'),
        }
        data = self.fetch_news(api_params)
        return Response(data)