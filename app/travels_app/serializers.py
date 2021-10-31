from rest_framework import serializers

from core.models import Travel


class TravelSerializer(serializers.ModelSerializer):
    """Serializer for travel objects"""
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Travel
        fields = "__all__"
        read_only_fields = ('id',)
