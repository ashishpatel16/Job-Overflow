from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import JobForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import JobPost
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from seekers.models import AppliedJobs
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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


def search_by_company(request, company_name):
    found = []
    for job in JobPost.objects.filter(company=company_name):
        found.append(job)
    return render(request, 'jobs/search_results.html', {'search_results': job})


def search(request):
    keyword = request.GET.get('key')
    company = request.GET.get('com')
    loc = request.GET.get('loc')
    jobs = []
    for job in JobPost.objects.filter(company=company, location=loc).order_by('-date_posted'):
        jobs.append(job)

    return render(request, 'jobs/search_results.html', {'searched_jobs': jobs})


def search_by_title(request):
    pass


def search_by_skill():
    pass
