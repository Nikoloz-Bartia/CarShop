from django.contrib import admin
from .models import *

admin.site.register([Condition, Category, Cars, Car])

admin.site.index_title = "CarShop Models"
admin.site.site_header = "CarShop"
admin.site.site_title = "CarShop"

