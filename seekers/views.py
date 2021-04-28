from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import JobSeeker, Skill, SavedJobs, AppliedJobs
from .forms import ProfileForm, SkillUpdateForm
from django.contrib.auth.models import User
from jobs.models import JobPost
from django.contrib import messages

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
        'form_skill': form_skill,
        'applied_jobs': get_applied_jobs(logged_user)
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


@login_required
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


@login_required
def apply(request, job_id):
    applicant = request.user
    # Tables to update : Applicants, AppliedJobs
    selected_job = JobPost.objects.filter(id=job_id).first()
    if AppliedJobs.objects.filter(user=applicant, job=selected_job):
        messages.warning(
            request, "Luckily You've already applied to this job.")
    else:
        messages.success(
            request, f'Congratulations! You succesfully applied to {selected_job.title}.')
        applied_job = AppliedJobs(job=selected_job, user=applicant)
        applied_job.save()
    return redirect('jobs-detail', pk=job_id)


def get_applied_jobs(user):
    applicant = user
    jobs = []
    for job in AppliedJobs.objects.filter(user=applicant):
        jobs.append(job)

    return jobs
