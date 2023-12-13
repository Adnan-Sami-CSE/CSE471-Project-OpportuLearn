from django.shortcuts import render, redirect
from .models import Category, Course, Booking, VisitorNotification
from . forms import AddCategory, AddCourse, BookingForm
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    notification = VisitorNotification.objects.all()
    category = Category.objects.all()
    course = Course.objects.all()
    context = {
        'category': category,
        'course': course,
        'notification': notification,
    }
    return render(request, 'home.html', context)


def add_category(request):
    if request.method == 'POST':
        form = AddCategory(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_course')
    else:
        form = AddCategory()

    context = {
        'form': form,
    }
    return render(request, 'add_category.html', context)


def add_course(request):
    if request.method == 'POST':
        form = AddCourse(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AddCourse()

    context = {
        'form': form,
    }
    return render(request, 'add_course.html', context)


@login_required
def book_course(request, course_id):
    course = Course.objects.get(id=course_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.course = course
            booking.save()
            return redirect('home')
    else:
        form = BookingForm()

    context = {
        'form': form,
        'course': course,
    }
    return render(request, 'book_course.html', context)


def booking_list(request):
    booking = Booking.objects.all()
    return render(request, 'booking.html', {'booking': booking})
