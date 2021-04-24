from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    context = {'title': 'Job Overflow'}
    return render(request, 'jobs/home.html', context)


def post_job(request):
    context = {'title': 'Post Job'}
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
