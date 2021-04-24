from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class JobPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=255)
    link = models.URLField(null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
