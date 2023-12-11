from django.contrib import admin
from .models import Category, Course, Booking, PaymentConfirmation
# Register your models here.

admin.site.register([Category, Course, Booking])

admin.site.register(PaymentConfirmation)