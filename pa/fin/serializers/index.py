"""
The Index model serializer
"""
from django.db.models import DecimalField, F, Count
from django.db.models.functions import Cast
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from fin.models.index import Ticker, TickerIndexWeight, Index
from fin.serializers.utils import FlattenMixin


class TickerSerializer(serializers.ModelSerializer):
    """
    Serialization class for the Ticker model
    """

    class Meta:
        model = Ticker
        fields = ['company_name', 'symbol', 'price', 'industry', 'sector', 'country']
from fin.models.index import Index
from fin.models.utils import MAX_DIGITS, DECIMAL_PLACES


class IndexSerializer(serializers.ModelSerializer):
    """
    Serialization class for the relation between indexes and tickers
    """
    id = serializers.IntegerField(read_only=True)
    industries_breakdown = SerializerMethodField(read_only=True)
    name = serializers.SerializerMethodField()
    sectors_breakdown = SerializerMethodField(read_only=True)

    def get_industries_breakdown(self, obj):
        """
        Returns list of industries and their percentage in the portfolio
        """
        decimal_field = DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)

        count = float(obj.tickers.count())
        query = obj.tickers.values('industry') \
            .annotate(percentage=Cast(Count('industry') / count * float(100), decimal_field))
        return query

    def get_name(self, obj):
        return dict(Index.Source.choices)[obj.data_source_url]

    def get_sectors_breakdown(self, obj):
        """
        Returns list of sectors and their percentage in the portfolio
        """
        decimal_field = DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)

        count = float(obj.tickers.count())
        query = obj.tickers.values('sector') \
            .annotate(percentage=Cast(Count('sector') / count * float(100), decimal_field))
        return query

    class Meta:
        model = Index
        fields = ('id', 'data_source_url', 'industries_breakdown', 'name', 'sectors_breakdown')


class AdjustedTickerSerializer(FlattenMixin, serializers.ModelSerializer):
    amount = serializers.SerializerMethodField()
    cost = serializers.SerializerMethodField()

    def get_amount(self, obj):
        return obj.amount

    def get_cost(self, obj):
        return obj.cost

    class Meta:
        model = TickerIndexWeight
        fields = ('amount', 'cost', 'weight')
        flatten = [('ticker', TickerSerializer)]

