from rest_framework.serializers import ModelSerializer

from core.models import Trip


class TripSerializer(ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'
        read_only_fields = ['user', 'created_at']  # Prevent manual setting of user and created_at
        depth = 1
