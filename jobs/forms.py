from django import forms
from .models import JobPost


class JobForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = "__all__"
        exclude = ['date_posted','recruiter']
