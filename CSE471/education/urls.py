from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_course/', views.add_course, name='add_course'),
    path('book_course/<int:course_id>/', views.book_course, name='book_course'),
    path('booking_list/', views.booking_list, name='booking_list'),

    # path('logout/', views.LogoutPage, name='logout'),
]
