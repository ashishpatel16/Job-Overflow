from django.db import models
from jobs.models import JobPost
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class JobSeeker(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, related_name='profile')
    full_name = models.CharField(max_length=200, blank=False)
    location = models.CharField(max_length=255, null=True, blank=True)
    resume = models.FileField(null=True, upload_to="resumes", blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Skill(models.Model):
    skill = models.CharField(max_length=200)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='skills')


class SavedJobs(models.Model):
    job = models.ForeignKey(
        JobPost, on_delete=models.CASCADE, related_name='saved_jobs')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='saved_by')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.job.title} job saved by {self.user.username}"


class AppliedJobs(models.Model):
    job = models.ForeignKey(
        JobPost, on_delete=models.CASCADE, related_name='applied_jobs')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='applicant')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.job.title} job applied by {self.user.username}"
