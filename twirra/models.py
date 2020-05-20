from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=280)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.author

    def get_absolute_url(self):
        return reverse('twirra-home')



