from rest_framework import serializers
from quotefetch.models import Quote


class FetchQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ["quote", "author"]
