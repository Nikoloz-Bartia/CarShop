from django.contrib import admin
from django.urls import path, include
from cars.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', include('cars.urls')),
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_view, name='logout'),
    

]

