from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    tag = models.CharField(max_length=255)
    description = models.TextField(blank=True , null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    remind_me_at = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.description