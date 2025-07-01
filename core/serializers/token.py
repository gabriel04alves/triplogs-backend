from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'

    def validate(self, attrs):
        # Força o uso do campo 'email' ao invés de 'username'
        attrs['username'] = attrs.get('email')
        return super().validate(attrs)
