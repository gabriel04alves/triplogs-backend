from rest_framework_simplejwt.views import TokenObtainPairView
from core.serializers.token import CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
