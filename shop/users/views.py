from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from users.forms import UserLoginForm, UserRegisterForm, UserProfileChangeForm
from django.urls import reverse
from .models import User



# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('allproducts'))
        else:
            messages.error(request, 'Invalid username or password.')
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserLoginForm()
    context = {'title': 'Войти', 'form': form,}
    return render(request, 'users/login.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST, files=request.FILES)
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        for user in User.objects.all():
            if user.username == request.POST['username']:
                messages.error(request, 'Username already taken.')
                return HttpResponseRedirect(reverse('registration'))
        if password1 == password2:
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('login'))
            else:
                messages.error(request, 'Please correct the error below.')
                return HttpResponseRedirect(reverse('registration'))
        else:
            messages.error(request, 'Passwords do not match.')
            return HttpResponseRedirect(reverse('registration'))
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'users/registration.html', context)

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('allproducts'))

@login_required(login_url='login')
def update(request):
    if request.method == 'POST':
        form = UserProfileChangeForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('allproducts'))
    else:
        form = UserProfileChangeForm(instance=request.user)
    context = {'form': form}
    return render(request, 'users/kabinet.html', context)
