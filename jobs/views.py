from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import JobForm, JobApplicationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import JobPost, JobApplication
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from seekers.models import AppliedJobs
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from collections import OrderedDict
# Create your views here.


def testimonials(request):
    return render(request, 'jobs/testimonials.html')


@login_required
def post_job(request):
    context = {
        'title': 'Post Job',
        'form': JobForm()
    }
    return render(request, 'jobs/post_job.html', context)


def hire(request):
    context = {'title': 'Hire someone'}
    return render(request, 'jobs/hire.html', context)


def contact(request):
    context = {'title': 'Contact Us'}
    return render(request, 'jobs/contact.html', context)


def about(request):
    context = {'title': 'About Us'}
    return render(request, 'jobs/about.html', context)


class JobListView(ListView):
    model = JobPost
    template_name = 'jobs/home.html'
    context_object_name = 'jobs'
    ordering = ['-date_posted']
    paginate_by = 5


class JobCreateView(LoginRequiredMixin, CreateView):
    model = JobPost
    fields = ['title', 'description', 'company', 'location']

    def form_valid(self, form):
        form.instance.recruiter = self.request.user
        return super().form_valid(form)


class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = JobPost
    fields = ['title', 'description', 'company', 'location']

    def form_valid(self, form):
        form.instance.recruiter = self.request.user
        return super().form_valid(form)

    def test_func(self):
        job = self.get_object()
        if job.recruiter == self.request.user:
            return True
        else:
            return False


class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = JobPost
    success_url = '/'

    def test_func(self):
        job = self.get_object()
        if job.recruiter == self.request.user:
            return True
        else:
            return False


class JobDetailView(DetailView):
    model = JobPost

    def get_context_data(self, **kwargs):
        context = super(JobDetailView, self).get_context_data(**kwargs)
        logged_user = self.request.user
        jobpost = self.get_object()
        if AppliedJobs.objects.filter(job=jobpost, user=logged_user).first() != None:
            context['has_applied'] = 1
        return context


def search(request):
    keyword = request.GET.get('key')
    company = request.GET.get('com')
    loc = request.GET.get('loc')
    jobs = []
    if company != "":
        for job in JobPost.objects.filter(company__iexact=company).order_by('-date_posted'):
            jobs.append(job)

    if loc != "":
        for job in JobPost.objects.filter(location__iexact=loc).order_by('-date_posted'):
            jobs.append(job)

    if keyword != "":
        for job in JobPost.objects.filter(title__icontains=keyword).order_by('-date_posted'):
            jobs.append(job)
        for job in JobPost.objects.filter(description__icontains=keyword).order_by('-date_posted'):
            jobs.append(job)

    p = Paginator(jobs, 10)
    page_num = request.GET.get('page')
    page_obj = p.get_page(page_num)

    context = {
        'searched_jobs': jobs,
        'page_obj': page_obj,
        'link': f'&key={keyword}&com={company}&loc={loc}'
    }

    return render(request, 'jobs/search_results.html', context)


@login_required
def apply(request, job_id):
    applicant = request.user

    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid:
            job = JobPost.objects.filter(id=job_id).first()
            application = form.save(commit=False)
            application.job = job
            AppliedJobs(job=job, user=applicant).save()
            application.applicant = applicant
            application.save()
            messages.success(
                request, f'Congratulations! You succesfully applied to {job.title}.')
            return redirect('jobs-detail', pk=job_id)
    else:
        form = JobApplicationForm()
    context = {
        'form': form,
    }
    return render(request, 'jobs/job_application.html', context)


class JobApplicationDetailView(DetailView):
    model = JobApplication

    def get_context_data(self, **kwargs):
        context = super(JobApplicationDetailView,
                        self).get_context_data(**kwargs)
        logged_user = self.request.user
        application = self.get_object()
        if logged_user == application.job.recruiter:
            context['is_recruiter'] = 1
        return context


def view_applications(request, pk):
    obj = JobApplication.objects.filter(id=pk)
    logged_user = request.user
    rec = obj.first().job.recruiter
    if logged_user == rec:
        is_rec = 1

    context = {
        'applications': obj,
        'object': JobPost.objects.filter(id=pk).first(),
        'is_recruiter': is_rec
    }
    return render(request, 'jobs/view_applications.html', context)
