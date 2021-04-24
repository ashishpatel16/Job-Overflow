from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        default='default.png', upload_to='profile_pics')
    full_name = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    is_recruiter = models.BooleanField(default=False, blank=False)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def save(self):
        super().save()

        img = Image.open(self.profile_picture.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_picture.path)
