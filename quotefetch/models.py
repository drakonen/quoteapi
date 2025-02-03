from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Quote(models.Model):
    retrieved_data = models.TextField()
    sent_data = models.TextField()
    quote = models.TextField()
    author = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.quote