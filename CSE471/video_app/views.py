from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
  return render(request, 'dashboard.html', {'name': request.user.username})

@login_required
def videocall(request):
    return render(request, 'videocall.html', {'name': request.user.username})

@login_required
def join_room(request):
    if request.method == 'POST':
        roomID = request.POST['roomID']
        return redirect("/meeting?roomID=" + roomID)
    return render(request, 'joinroom.html')

