from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('meeting/',views.videocall, name='meeting'),
    path('join/',views.join_room, name='join_room'),
]
