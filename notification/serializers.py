from .models import Notification
from rest_framework import serializers

class NotificationSerialier(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields ="__all__"
