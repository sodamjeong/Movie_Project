from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm, CustomUserCreationForm, CustomAuthenticationForm
from .models import User
import os
from django.conf import settings

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('reivews:index')
    login_form = AuthenticationForm()
    if request.method == 'POST':
        signup_form = CustomUserCreationForm(request.POST, request.FILES)
        if signup_form.is_valid():
            signup_form.save()
            return redirect('reviews:index')
    else:
        signup_form = CustomUserCreationForm()
    
    context = {
        'signup_form': signup_form, 
        'login_form': login_form,
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('reviews:index')
    
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('reviews:index')

@login_required
def logout(request):
    auth_logout(request)
    return redirect('reviews:index')

@login_required
def update(request):
    # user = User.objects.get(pk=request.user.pk)
    if request.method == 'POST':
        # file_change_check = request.POST.get('fileChange', False)
        # file_check = request.POST.get('upload_files-clear', False)
        # if file_change_check or file_check:
        #     os.remove(os.path.join(settings.MEDIA_ROOT, user.profile_image.path))
        
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:mypage', request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
        
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)

@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('reviews:index')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('reviews:index')
    else:
        form = PasswordChangeForm(request.user)
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)

@login_required
def mypage(request, accounts_pk):
    user = User.objects.get(pk=accounts_pk)
    context = {
        'user': user,
    }
    return render(request, 'accounts/mypage.html', context)