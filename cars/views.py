from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .forms import RegisterForm, CarForm
from .models import *


# Create your views here.

def home(request):
    objects = Cars.objects.all() 
    return render(request, 'home.html', {'objects':objects})


def cars(request):
    data = Cars.objects.all()
    item = Car.objects.all()
    return render(request, 'cars.html', {'data': data, 'item': item}) 



def pk_cars(request, pk):
    # მანქანის მოძებნა ან 404 შეცდომის დაბრუნება, თუ არ მოიძებნა
    car = get_object_or_404(Cars, pk=pk)
    return render(request, 'pk_cars.html', {'car': car})



def register(request):
    
    if request.user.is_authenticated:
        return redirect('dashboard')


    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = RegisterForm()

    form = UserCreationForm()
    return render(request, 'register.html', {'form':form})



def login(request):

    if request.user.is_authenticated:
        return redirect('dashboard')


    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)  # მომხმარებლის ავტენტიფიკაცია
                return redirect('dashboard')  # შეცვალეთ 'target_url' თქვენი მიზნობრივი URL-ით
            else:
                messages.error(request, "Invalid username or password.")
    
    else:
        form = AuthenticationForm()        
    
    return render(request, 'login.html', {'form': form})



def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('home')


def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()  # ფორმის მონაცემების შენახვა
            return redirect('cars')  # გადამისამართება მანქანების სიაზე (შექმენი car_list URL)
    else:
        form = CarForm()
    
    return render(request, 'add_car.html', {'form': form})




