from django.http import FileResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CertificateForm
from django.conf import settings

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


@user_passes_test(lambda u: u.is_staff)
def add_certificate(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST)
        if form.is_valid():
            certificate = form.save()
            return redirect('/admin')  
    else:
        form = CertificateForm()

    return render(request, 'add_certificate.html', {'form': form})


# def pdf_view(request):
#     # Path to your PDF file
#     pdf_path = os.path.join(settings.MEDIA_ROOT, 'certificates', 'certificate.pdf')
    
#     # Open the PDF file in binary mode
#     with open(pdf_path, 'rb') as pdf_file:
#         response = FileResponse(pdf_file, content_type='application/pdf')
#         response['Content-Disposition'] = 'filename="certificate.pdf"'
#         return response

