from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('meeting/',views.videocall, name='meeting'),
    path('join/',views.join_room, name='join_room'),
    path('add_certificate/', views.add_certificate, name='add_certificate'),
    path('add_StudentCourse/', views.add_StudentCourse, name='add_StudentCourse'),
    # path('pdf_view/', views.pdf_view, name='pdf_view'),
]
