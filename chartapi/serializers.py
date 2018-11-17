from .models import Stock_9432
from rest_framework import serializers


class Stock_9432Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stock_9432
        fields = (
                    'time',
                    'opening_price',
                    'high_price',
                    'low_price',
                    'closing_price',
                    'volume',
                    'ad_closing_price'
                )
