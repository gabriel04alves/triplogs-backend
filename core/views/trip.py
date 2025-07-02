from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django.core.exceptions import PermissionDenied

from core.models import Trip
from core.serializers import TripSerializer


class TripViewSet(ModelViewSet):
    serializer_class = TripSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Return trips for the authenticated user only."""
        return Trip.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        """Set the user to the current authenticated user when creating a trip."""
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        """Ensure user can only update their own trips."""
        if serializer.instance.user != self.request.user:
            raise PermissionDenied("You can only update your own trips.")
        serializer.save()

    def perform_destroy(self, instance):
        """Ensure user can only delete their own trips."""
        if instance.user != self.request.user:
            raise PermissionDenied("You can only delete your own trips.")
        instance.delete()
