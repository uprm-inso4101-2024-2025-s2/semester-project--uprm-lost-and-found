from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import User
import json

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            User.objects.create(
                U_Username=data['username'],
                U_Email=data['email'],
                U_FullName=data['fullName'],
                U_Password=data['password'],
                U_Occupation=data['occupation']
            )
            return JsonResponse({'message': 'Account created successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

from django.shortcuts import render

def signup_form(request):
    return render(request, 'accounts/signup.html')

def login_form(request):
    return render(request, 'accounts/login.html')

# Log in handler
@csrf_exempt
def login_check(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        try:
            user = User.objects.get(U_Email=email, U_Password=password)
            return JsonResponse({'message': f'Welcome, {user.U_FullName}'}, status=200)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Invalid email or password'}, status=401)