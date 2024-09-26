import requests

class DataCollection:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://newsapi.org/v2/everything'

    def fetch_news(self, query, from_date, to_date, language='en'):
        params = {
            'q': query,
            'from': from_date,
            'to': to_date,
            'language': language,
            'apiKey': self.api_key
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()['articles']
        else:
            return None
