from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import JobSeeker, Skill, SavedJobs, AppliedJobs
from .forms import ProfileForm, SkillUpdateForm
from django.contrib.auth.models import User

# Create your views here.


@login_required
def my_profile(request):
    logged_user = request.user
    user_profile = JobSeeker.objects.filter(user=logged_user).first()
    skillset = []
    for skill_name in Skill.objects.filter(user=logged_user):
        skillset.append(skill_name.skill)

    if request.method == 'POST':
        form_profile = ProfileForm(
            request.POST, request.FILES, instance=user_profile)
        form_skill = SkillUpdateForm(request.POST)
        if form_profile.is_valid() and form_skill.is_valid():
            profile_data = form_profile.save(commit=False)
            profile_data.user = logged_user
            profile_data.save()
            skill_data = form_skill.save(commit=False)
            if not skill_data.skill == None:
                skill_data.user = logged_user
                skill_data.save()
            return redirect('my-profile')
    else:
        form_profile = ProfileForm(instance=user_profile)
        form_skill = SkillUpdateForm()
    context = {
        'logged_user': logged_user,
        'user_profile': user_profile,
        'user_skills': skillset,
        'form_profile': form_profile,
        'form_skill': form_skill
    }
    return render(request, 'seekers/my_profile.html', context)


def view_profile(request, user_id):
    user = User.objects.filter(pk=user_id).first()
    user_profile = JobSeeker.objects.filter(user=user).first()
    skillset = []
    for skill in Skill.objects.filter(user=user):
        skillset.append(skill)

    context = {
        'user': user,
        'user_profile': user_profile,
        'user_skills': skillset
    }
    return render(request, 'seekers/profile_detail.html', context)


def add_skill(request):
    user = request.user
    if request.method == "POST":
        form = SkillUpdateForm(request.POST)
        if form.is_valid():
            skill_data = form.save(commit=False)
            skill_data.user = user
            skill_data.save()
            return redirect('my-profile')
    else:
        form = SkillUpdateForm()
    return render(request, 'seekers/add_skill.html', {'form': form})
