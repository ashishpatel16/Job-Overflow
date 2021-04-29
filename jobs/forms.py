from django import forms
from .models import JobPost, JobApplication


class JobForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = "__all__"
        exclude = ['date_posted', 'recruiter']


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['full_name', 'email', 'address', 'additional_info', 'resume']
        exclude = ['date_applied', 'job', 'applicant']
        help_texts = {
            'additional_info': ('Strengthen your profile! Mention past experiences, awards or achievements you accomplished in this domain.'),
        }
