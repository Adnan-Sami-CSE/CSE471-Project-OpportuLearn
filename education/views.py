from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Course, Booking, Query, PaymentConfirmation
from . forms import AddCategory, AddCourse, BookingForm, QueryForm
from django.contrib.auth.decorators import login_required, user_passes_test
from video_app.models import Certificate, StudentCourse

# Create your views here.


def home(request):
    category = Category.objects.all()
    course = Course.objects.all()
    context = {
        'category': category,
        'course': course,
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

def DisplayCoursesPage(request):
    return render(request, "displaycourses.html")

def CourseDetails01(request):
    return render(request, "coursedetails01.html")

def CourseDetails01(request):
    return render(request, "coursedetails01.html")

def CourseDetails02(request):
    return render(request, "coursedetails02.html")

def CourseDetails03(request):
    return render(request, "coursedetails03.html")

def StudentHome(request):
    user_certificates = Certificate.objects.filter(user=request.user)
    user_courses = StudentCourse.objects.filter(user=request.user)
    user_course_playlist = StudentCourse.objects.filter(user=request.user)
    user_type_name= StudentCourse.objects.filter(user=request.user)
    return render(request, "studenthome.html", {'email': request.user.email, 'user_certificates': user_certificates,'user_courses': user_courses,'user_course_playlist':  user_course_playlist,'user_type_name':  user_type_name, })   


# Post Q/A
@login_required
def add_query(request):
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            query = form.save(commit=False)
            query.user = request.user
            query.save()
            return redirect('query_detail', query_id=query.id)  
    else:
        form = QueryForm()

    return render(request, 'qa_page1.html', {'form': form})


def query_detail(request, query_id):
    query = Query.objects.get(pk=query_id)
    return render(request, 'qa_page2.html', {'query': query})


def all_queries(request):
    queries = Query.objects.all()
    return render(request, 'qa_page3.html', {'queries': queries})


@user_passes_test(lambda u: u.is_staff)
def delete_query(request, query_id):
    query = Query.objects.get(pk=query_id)
    if request.method == 'POST':
        query.delete()
        return redirect('all_queries')
    return render(request, 'qa_page4.html', {'query': query})


    # payment by code
def payment_confirmation(request):
    return render(request, 'payment_confirmation.html')

def confirm_payment(request):
    if request.method == 'POST':
        secret_code = '5678'  # replacable code
        confirmation_code = request.POST.get('confirmation_code')
        username = request.POST.get('username')  # Extract username from the form data

        if confirmation_code == secret_code:
            # Save the data to the database
            PaymentConfirmation.objects.create(confirmation_code=confirmation_code, username=username)

            return redirect('payment_success')
        else:
            return redirect('payment_error')
    return redirect('payment_confirmation')

def payment_success(request):
    return render(request, 'payment_success.html')

def payment_error(request):
    return render(request, 'payment_error.html')
