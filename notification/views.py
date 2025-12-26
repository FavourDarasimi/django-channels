from django.shortcuts import render
from .serializers import NotificationSerialier
from .models import Notification
from rest_framework.generics import ListCreateAPIView
from send.utils import broadcast_notification

class NotificationView(ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerialier

    def perform_create(self, serializer):
        notification = serializer.save()

        broadcast_notification({
            "event": "post_created",
            "post": NotificationSerialier(notification).data,
        })
# Create your views here.
