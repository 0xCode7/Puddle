from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignupForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created!')
            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'auth/signup.html', {'form': form})
