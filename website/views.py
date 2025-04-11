from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(U_Username=username)
            if user.U_Password == password:
                return redirect('dashboard')  # or any success page
            else:
                messages.error(request, 'Incorrect password.')
        except User.DoesNotExist:
            messages.error(request, 'Account does not exist.')
    
    return render(request, 'login.html')