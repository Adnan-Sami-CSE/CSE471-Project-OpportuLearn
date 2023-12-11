from django import forms
from .models import Certificate, StudentCourse

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['user', 'course_name']

class StudentCourseForm(forms.ModelForm):
    class Meta:
        model = StudentCourse
        fields = ['user', 'course_name', 'course_playlist', 'type_name']