import requests
from rest_framework import serializers
from django.conf import settings
from quotefetch.models import Quote

class FetchQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ['quote', 'author']