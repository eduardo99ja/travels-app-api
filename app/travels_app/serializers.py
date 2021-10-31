from django.db.models import fields
from rest_framework import serializers


from core.models import Travel, Category


class TravelSerializer(serializers.ModelSerializer):
    """Serializer for travel objects"""
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Travel
        fields = "__all__"
        read_only_fields = ('id',)


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for category objects"""

    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ('id',)
