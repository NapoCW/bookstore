from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('already_logged_in') 
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
                return redirect('home') 
            messages.error(request, "There was an error in the form. Please try again.")
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('already_logged_in')  
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in!")
                return redirect('home') 
            else:
                messages.error(request, "Invalid credentials. Please try again.")
        else:
            messages.error(request, "There was an error in the form. Please try again.")
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def already_logged_in_view(request):
    return render(request, 'accounts/already_logged_in.html', {'username': request.user.username})

def logout_view(request):
    logout(request)
    return  render(request, 'accounts/logout.html', {'username': request.user.username})

@login_required
def view_personal_info(request):
    user = request.user
    return render(request, 'accounts/view_personal_info.html', {'user': user})

@login_required
def edit_personal_info(request):
    user = request.user
    if request.method == 'POST':
        user.username = request.POST.get('username')
        new_password = request.POST.get('password')
        if new_password:
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Your information has been updated successfully.')
            return redirect('view_personal_info')

        user.save()
        messages.success(request, 'Your information has been updated successfully.')
        return redirect('view_personal_info')
    
    return render(request, 'accounts/edit_personal_info.html', {'user': user})