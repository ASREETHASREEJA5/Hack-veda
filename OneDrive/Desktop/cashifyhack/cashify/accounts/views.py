from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import HttpResponseRedirect
from django.contrib import messages
from .models import MobileDevice
from .forms import MobileDeviceForm

  
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully. You can now log in.')
            return redirect('signin')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})


def base(request):
    return render(request, 'base.html')
def home(request): 
    devices = MobileDevice.objects.all()
    return render(request, 'profile1.html', {'devices': devices})

def add_device(request):
    if request.method == 'POST':
        form = MobileDeviceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile1')
    else:
        form = MobileDeviceForm()
    return render(request, 'add_device.html', {'form': form})

def delete_device(request):
    if request.method == 'POST':
        devices_to_delete = request.POST.getlist('devices_to_delete')
        MobileDevice.objects.filter(id__in=devices_to_delete).delete()
    return redirect('profile1')

  
def signin(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile1') #profile
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
  
def profile(request):
    devices = MobileDevice.objects.all()
    return render(request, 'profile1.html',{'devices': devices})
   
def signout(request):
    logout(request)
    return redirect('/')