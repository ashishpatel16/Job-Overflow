from django.contrib import admin
from .models import JobSeeker, AppliedJobs, SavedJobs, Skill

# Register your models here.
admin.site.register(JobSeeker)
admin.site.register(AppliedJobs)
admin.site.register(SavedJobs)
admin.site.register(Skill)
