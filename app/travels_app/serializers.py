from django.db.models import fields
from rest_framework import generics, serializers
from rest_framework.fields import ReadOnlyField
from rest_framework.relations import PrimaryKeyRelatedField, StringRelatedField


from core.models import Travel, Category


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for category objects"""

    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ('id',)


class TravelSerializer(serializers.ModelSerializer):
    """Serializer for travel objects"""
    user = serializers.StringRelatedField(read_only=True)
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all())

    class Meta:
        model = Travel
        fields = "__all__"
        read_only_fields = ('id',)


class TravelCategorySerializer(serializers.ModelSerializer):
    """Serializer for travel objects"""
    user = serializers.StringRelatedField(read_only=True)
    category = CategorySerializer()

    class Meta:
        model = Travel
        fields = "__all__"
        read_only_fields = ('id',)
