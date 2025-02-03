import requests

from django.conf import settings
from drf_excel.mixins import XLSXFileMixin

from rest_framework import viewsets
from rest_framework.decorators import action, authentication_classes, permission_classes
from rest_framework.response import Response

from quotefetch.models import Quote
from quotefetch.serializers import FetchQuoteSerializer


class QuoteViewSet(XLSXFileMixin, viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = FetchQuoteSerializer
    filename = 'quotes.xlsx'


    # get
    def list(self, request):
        queryset = Quote.objects.all()
        serializer = FetchQuoteSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def random(self, request):
        # get source from header
        source = request.headers.get('source', 'dummyjson')

        if source not in settings.QUOTE_API_ENDPOINTS.keys():
            raise ValueError('Invalid source')

        api_url = settings.QUOTE_API_ENDPOINTS[source]

        print("api_url: ", api_url)

        # get quote from api
        response = requests.get(api_url['url'])
        response_data = response.json()

        print("response_data: ", response_data)

        # hardcoded for now
        if source == 'dummyjson':
            quote_text = response_data['quote']
            author = response_data['author']
        elif source == 'zenquotes':
            quote_text = response_data[0]['q']
            author = response_data[0]['a']

        # create temp quote object
        quote = Quote.objects.create(
            quote=quote_text,
            author=author,
            retrieved_data=response_data
        )

        # return quote
        serializer = FetchQuoteSerializer(quote)
        response = Response(serializer.data)

        # update quote object
        quote.sent_data = response.data
        quote.save()

        return response

    def list(self, request):
        queryset = Quote.objects.all()
        serializer = FetchQuoteSerializer(queryset, many=True)
        return Response(serializer.data)

    # def create(self, request):
    #     serializer = FetchQuoteSerializer(data=request.data, context={'request': request})
    #     serializer.is_valid(raise_exception=True)
    #     quote = serializer.save()
    #     return Response(quote)