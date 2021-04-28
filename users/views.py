from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm
# Create your views here.


def register(request):
    if request.method == 'POST':
        # If already some data is filled, keep them
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, "Account Successfully Created for {}!".format(username))
            return redirect('jobs-home')
    else:
        # This is trigerred by GET requests, hence return a new empty Form object
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


