"""
URL configuration for registration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('forgotpass/',views.ForgotPass,name='forgotpass'),
    path('displaycourses/',views.DisplayCoursesPage,name='displaycourses'),
    path('coursedetails01/',views.CourseDetails01,name='coursedetails01'),
    path('coursedetails02/',views.CourseDetails02,name='coursedetails02'),
    path('coursedetails03/',views.CourseDetails03,name='coursedetails03'),
    path('studenthome/',views.StudentHome,name='studenthome'),
    path('qa_page/', views.qa_page, name='qa_page'),
    path('payment_confirmation/', views.payment_confirmation, name='payment_confirmation'),
    path('confirm_payment/', views.confirm_payment, name='confirm_payment'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('payment_error/', views.payment_error, name='payment_error'),
]

