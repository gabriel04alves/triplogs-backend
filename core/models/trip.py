"""
Trip model.
"""

from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import User


class Trip(models.Model):
    """Trip model to store travel records associated with each user."""

    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        verbose_name=_('user'), 
        help_text=_('Reference to the user who owns the trip.')
    )
    title = models.CharField(
        max_length=100, 
        verbose_name=_('title'), 
        help_text=_('Title or name of the trip (e.g., "Vacation in Paris").')
    )
    location = models.CharField(
        max_length=100, 
        verbose_name=_('location'), 
        help_text=_('Destination of the trip (e.g., "Paris, France").')
    )
    trip_date = models.DateField(
        verbose_name=_('trip date'), 
        help_text=_('Date when the trip took place.')
    )
    description = models.TextField(
        blank=True, 
        null=True, 
        verbose_name=_('description'), 
        help_text=_('Additional details or notes about the trip.')
    )
    photo = models.TextField(
        blank=True, 
        null=True, 
        verbose_name=_('photo'), 
        help_text=_('Photo related to the trip uploaded by the user.')
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name=_('created at'), 
        help_text=_('Timestamp when the trip entry was created.')
    )

    class Meta:
        """Meta options for the model."""
        
        verbose_name = _('Trip')
        verbose_name_plural = _('Trips')
        ordering = ['-created_at']

    def __str__(self):
        """String representation of the trip."""
        return f'{self.title} - {self.location}'
