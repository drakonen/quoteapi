import json
from unittest import mock

from django.urls import reverse

from rest_framework.test import APITestCase

# Create your tests here.

# mock the requests.get method
def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == 'https://zenquotes.io/api/random':
        mockdata = json.load(open('quotefetch/tests/fixtures/zenquotes.json'))
        return MockResponse(mockdata, 200)
    elif args[0] == 'https://dummyjson.com/quotes/random':
        mockdata = json.load(open('quotefetch/tests/fixtures/dummyjson.json'))
        return MockResponse(mockdata, 200)

    return MockResponse(None, 404)


class QuoteTest(APITestCase):
    url = reverse('quote-random')

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_quote_random(self, mock_get):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['quote'], 'If you want to lift yourself up, lift up someone else.')


        response2 = self.client.get(self.url, headers={'source': 'zenquotes'})
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response2.data['quote'], 'When you believe in a thing, believe in it all the way, implicitly and unquestionable.')
