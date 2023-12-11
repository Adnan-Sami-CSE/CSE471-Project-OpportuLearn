from django.contrib import admin
from .models import Certificate, StudentCourse
# Register your models here.

admin.site.register([Certificate])

admin.site.register([StudentCourse])