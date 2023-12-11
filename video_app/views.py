from django.http import FileResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CertificateForm, StudentCourseForm
from django.conf import settings

# Create your views here.
@login_required
def dashboard(request):
  return render(request, 'dashboard.html', {'name': request.user.username})

@login_required
def videocall(request):
    return render(request, 'videocall.html', {'name': request.user.username})

@login_required
def join_room(request):
    if request.method == 'POST':
        roomID = request.POST['roomID']
        return redirect("/meeting?roomID=" + roomID)
    return render(request, 'joinroom.html')


@user_passes_test(lambda u: u.is_staff)
def add_certificate(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST)
        if form.is_valid():
            certificate = form.save()
            return redirect('/home')  
    else:
        form = CertificateForm()

    return render(request, 'add_certificate.html', {'form': form})


@user_passes_test(lambda u: u.is_staff)
def add_StudentCourse(request):
    if request.method == 'POST':
        form = StudentCourseForm(request.POST)
        if form.is_valid():
            StudentCourse = form.save()
            return redirect('/home')  
    else:
        form = StudentCourseForm()

    return render(request, 'add_StudentCourse.html', {'form': form})