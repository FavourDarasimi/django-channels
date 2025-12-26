from django.db import models

class Notification(models.Model):
    name = models.CharField(max_length=20)
    message = models.TextField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
