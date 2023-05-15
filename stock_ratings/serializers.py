from rest_framework import routers,serializers,viewsets
from .models import StockRating
class StockRatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StockRating
        fields = ['id', 'title', 'description', 'value', 'created_at']