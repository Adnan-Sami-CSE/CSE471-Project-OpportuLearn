from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=90)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Course(models.Model):

    CHOICE_ONE = 'Free'
    CHOICE_TWO = 'Paid'

    YOUR_CHOICES = [
        (CHOICE_ONE, 'Free'),
        (CHOICE_TWO, 'Paid'),
    ]

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=90)
    payment_category = models.CharField(
        max_length=10, choices=YOUR_CHOICES, default=CHOICE_ONE,)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.name}"


class Adding(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.course.name}"
    
class Query(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()



class PaymentConfirmation(models.Model):
    confirmation_code = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
