from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=255)


class StudentCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=255)
    type_name = models.CharField(max_length=255, default='')
    course_playlist = models.CharField(max_length=255, default='')