from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from . tokens import generate_token

from core import settings
# Create your views here.


@login_required(login_url='login')
def HomePage(request):
    return render(request, "home.html")


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        # print(uname, email, pass1, pass2)
        if User.objects.filter(username=uname):
            messages.error(request, "Username already exists! Please try some other username.")
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!")
            return redirect('signup')
        
        if pass1 != pass2:
            messages.error(request, "Password and confrim password are not Same!")
            return redirect('signup')
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.is_active = False
            my_user.save()
            messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
        
            # # Welcome Email
            # subject = "Welcome to OpportuLearn!"
            # message = "Hello " + my_user.first_name + "!\n" + "Welcome to OpportuLearn!\nThank you for signing up.\nWe have sent you a confirmation email to complete your registration.\n\nThanks\nOpportuLearn"        
            # from_email = settings.EMAIL_HOST_USER
            # to_list = [my_user.email]
            # send_mail(subject, message, from_email, to_list, fail_silently=True)
            
            # Email Address Confirmation Email
            current_site = get_current_site(request)
            email_subject = "Activate account | OpportuLearn"
            message2 = render_to_string('email_confirmation.html',{
                
                'name': my_user.first_name,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(my_user.pk)),
                'token': generate_token.make_token(my_user)
            })
            email = EmailMessage(
                email_subject,
                message2,
                settings.EMAIL_HOST_USER,
                [my_user.email],
            )
            email.fail_silently = True
            email.send()
            
            return redirect('login')

    return render(request, "signup.html")


def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        my_user = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        my_user = None

    if my_user is not None and generate_token.check_token(my_user,token):
        my_user.is_active = True
        # user.profile.signup_confirmation = True
        my_user.save()
        login(request,my_user)
        messages.success(request, "Your Account has been activated!")
        return redirect('login')
    else:
        messages.error(request, "Account activation failed!")
        return redirect('signup')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, "login.html")


def LogoutPage(request):
    logout(request)
    return redirect('login')


