from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail
import random


# Create your views here.

@login_required(login_url='login')
def HomePage(request):
    return render (request, "home.html")

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')


        if pass1!=pass2:
            return HttpResponse("Your password and confrim password are not Same!!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')

    return render (request, "signup.html")

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request, "login.html")

def LogoutPage(request):
    logout(request)
    return redirect('login')

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
    return render(request, "studenthome.html")

def ForgotPass(request):
    return render(request, "forgotpass.html")




# This part is for Q/A forum
questions = []  # Global questions

# views.py

from django.shortcuts import render, redirect

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


# Payment by email( not working)
# def payment_page(request):
#     return render(request, 'payment.html')

# def process_payment(request):
#     if request.method == 'POST':
#         confirmation_code = request.POST.get('confirmation_code')

#         # success
#         if confirmation_code.isdigit() and len(confirmation_code) == 4:
#             # email 
#             send_confirmation_email()

#             #success message
#             return render(request, 'payment_success.html')
    
#     # error message 
#     return render(request, 'payment_error.html')

# def send_confirmation_email():
#     # Simulating email 
#     subject = 'Course Added Confirmation'
#     message = 'Thank you for adding the course. Your payment was successful.'
#     from_email = 'adnan.sami@g.bracu.ac.bd'
#     recipient_list = ['adnansami1515@gmail.com']
#     send_mail(subject, message, from_email, recipient_list)




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