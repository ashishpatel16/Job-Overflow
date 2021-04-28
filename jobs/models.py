from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class JobPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    recruiter = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=200, default="")
    location = models.CharField(max_length=255)
    link = models.URLField(null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    skills_req = models.CharField(
        max_length=200, default="No skills required.", null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('jobs-home')


class Applicants(models.Model):
    job = models.ForeignKey(
        JobPost, related_name='applicants', on_delete=models.CASCADE)
    applicant = models.ForeignKey(
        User, related_name='applied_by', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.applicant


class Selected(models.Model):
    job = models.ForeignKey(
        JobPost, related_name='selected_for', on_delete=models.CASCADE)
    applicant = models.ForeignKey(
        User, related_name='selected_applicant', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.applicant
