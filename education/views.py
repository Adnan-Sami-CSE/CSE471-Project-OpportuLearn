from django.shortcuts import render, redirect
from .models import Category, Course, Booking
from . forms import AddCategory, AddCourse, BookingForm
from django.contrib.auth.decorators import login_required
from video_app.models import Certificate

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
    return render(request, "studenthome.html", {'email': request.user.email, 'user_certificates': user_certificates})   



#Post Q&A Part
questions = []  

def qa_page(request):
    global questions
    
    if request.method == 'POST':
        if 'question_text' in request.POST:
            #posting a new question
            question_text = request.POST.get('question_text')
            questions.append({'question_text': question_text, 'answers': []})
            return redirect('qa_page')
        elif 'answer_text' in request.POST:
            #posting an answer
            answer_text = request.POST.get('answer_text')
            question_id = int(request.POST.get('question_id'))
            questions[question_id]['answers'].append(answer_text)
            return redirect('qa_page')

    
    questions_data = [{'index': idx, 'question_text': question['question_text']} for idx, question in enumerate(questions)]

    return render(request, 'qa_page.html', {'questions_data': questions_data, 'questions': questions})


    # payment by code
def payment_confirmation(request):
    return render(request, 'payment_confirmation.html')

def confirm_payment(request):
    if request.method == 'POST':
        
        secret_code = '5678' # replacable code
        confirmation_code = request.POST.get('confirmation_code')
        if confirmation_code == secret_code:
            return redirect('payment_success')
        else:
            return redirect('payment_error')
    return redirect('payment_confirmation')

def payment_success(request):
    return render(request, 'payment_success.html')

def payment_error(request):
    return render(request, 'payment_error.html')





