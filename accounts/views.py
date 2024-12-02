from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

# Signup view
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('already_logged_in')  # Redirect to the "already logged in" page
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully signed up and are now logged in!")
                return redirect('home')  # Redirect to home page after successful signup
        else:
            messages.error(request, "There was an error in the form. Please try again.")
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

# Login view
def login_view(request):
    if request.user.is_authenticated:
        return redirect('already_logged_in')  # Redirect to the "already logged in" page
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in!")
                return redirect('home')  # Redirect to home page after successful login
            else:
                messages.error(request, "Invalid credentials. Please try again.")
        else:
            messages.error(request, "There was an error in the form. Please try again.")
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# View for already logged-in users
@login_required
def already_logged_in_view(request):
    return render(request, 'accounts/already_logged_in.html', {'username': request.user.username})

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to the home page after logout
