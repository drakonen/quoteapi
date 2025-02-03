import requests
from rest_framework import serializers
from django.conf import settings
from quotefetch.models import Quote

class FetchQuoteSerializer(serializers.Serializer):
    source = serializers.ChoiceField(choices=settings.QUOTE_API_ENDPOINTS.keys(), default='dummyjson')

    def create(self, validated_data):
        # check if valid source
        source = validated_data['source']
        if source not in settings.QUOTE_API_ENDPOINTS.keys():
            raise ValueError('Invalid source')

        api_url = settings.QUOTE_API_ENDPOINTS[source]

        # get quote from api
        response = requests.get(api_url)
        response_data = response.json()

        # hardcoded for now
        if source == 'dummyjson':
            quote_text = response_data['quote']
            author = response_data['author']
        elif source == 'zenquotes':
            quote_text = response_data[0]['q']
            author = response_data[0]['a']

        # store quote in db
        quote = Quote.objects.create(
            retrieved_data=response_data,
            sent_data=response_data,
            quote=quote_text,
            author=author,
            user=self.context['request'].user
        )

        return {
            'quote': quote.quote,
            'author': quote.author,
        }