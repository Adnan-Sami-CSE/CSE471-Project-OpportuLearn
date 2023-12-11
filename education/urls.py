from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_course/', views.add_course, name='add_course'),
    path('book_course/<int:course_id>/', views.book_course, name='book_course'),
    path('booking_list/', views.booking_list, name='booking_list'),
    path('studenthome/',views.StudentHome,name='studenthome'),
    # path('qa_page/', views.qa_page, name='qa_page'),
    path('coursedetails01/',views.CourseDetails01,name='coursedetails01'),
    path('coursedetails02/',views.CourseDetails02,name='coursedetails02'),
    path('coursedetails03/',views.CourseDetails03,name='coursedetails03'),
    path('payment_confirmation/', views.payment_confirmation, name='payment_confirmation'),
    path('confirm_payment/', views.confirm_payment, name='confirm_payment'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('payment_error/', views.payment_error, name='payment_error'),
    path('add_query/', views.add_query, name='add_query'),
    path('query_detail/<int:query_id>/', views.query_detail, name='query_detail'),
    path('all_queries/', views.all_queries, name='all_queries'),
    path('delete_query/<int:query_id>/', views.delete_query, name='delete_query'),
]
