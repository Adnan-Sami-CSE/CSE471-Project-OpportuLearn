from .models import Category, Course, Booking, Query
from django import forms
from django.contrib.auth.models import User


class AddCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

    def save(self, commit=True):
        instance = super(AddCategory, self).save(commit=False)
        instance.user = User.objects.get(username='admin')
        if commit:
            instance.save()
        return instance


class AddCourse(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['category', 'name',
                  'payment_category', 'payment_amount', 'note']


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['note']


class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ['content']

