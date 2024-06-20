# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def homepage_view(request):
    return render(request, 'myapp/homepage.html')

def signup_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.save()

            # Logic to send an email
            subject = 'Welcome to Our Website'
            message = 'Thank you for signing up!'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [email]

            try:
                send_mail(subject, message, from_email, recipient_list)
            except Exception as e:
                logger.error("Error sending email: %s", e)

            # Automatically log in the user after signup
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('userpage')

    return render(request, 'myapp/login.html')

def login_view(request):
    error = None
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('userpage')
        else:
            error = 'Invalid email or password'
    
    return render(request, 'myapp/login.html', {'error': error})

def userpage_view(request):
    return render(request, 'myapp/userpage.html')

# myapp/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def submit_cv(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        education = request.POST.get('education')
        experience = request.POST.get('experience')

        # Process and save CV data (example: save to database)

        return JsonResponse({'message': 'CV submitted successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'})
