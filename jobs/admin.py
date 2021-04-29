from django.contrib import admin
from .models import JobPost, Applicants, Selected, JobApplication

# Register your models here.
admin.site.register(JobPost)
admin.site.register(Applicants)
admin.site.register(Selected)
admin.site.register(JobApplication)
