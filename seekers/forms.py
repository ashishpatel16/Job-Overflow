from .models import JobSeeker, Skill
from django import forms
from django.forms import ModelForm, Textarea


class ProfileForm(forms.ModelForm):
    class Meta:
        model = JobSeeker
        fields = "__all__"
        exclude = ['user']

        


class SkillUpdateForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = "__all__"
        exclude = ['user']

        help_texts = {
            'skill': ('Add a new skill'),
        }
