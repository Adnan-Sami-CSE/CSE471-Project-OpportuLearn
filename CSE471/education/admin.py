from django.contrib import admin
from .models import Category, Course, Booking
# Register your models here.

admin.site.register([Category, Course, Booking])
