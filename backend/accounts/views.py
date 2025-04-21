from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import LostItem, User
from datetime import datetime
import json
import requests

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

def homepage(request):
    return render(request, 'accounts/index.html')

def found_item_page(request):
    return render(request, 'accounts/founditem.html')

def lost_item_page(request):
    return render(request, 'accounts/lostitem.html')

def report_type_page(request):
    return render(request, 'accounts/report-type.html')



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

@csrf_exempt
def submit_lost_item(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            description = data.get('description')
            location = data.get('lostLocation')
            comments = data.get('comments', '')
            email = data.get('contactEmail')
            images = data.get('images', [])

            # Build info
            l_info = f"{location} - {comments}"
            date_now = datetime.now().strftime("%Y-%m-%d")

            # Get user ID
            try:
                user = User.objects.get(U_Email=email)
                uid = user.U_ID
            except User.DoesNotExist:
                return JsonResponse({'error': 'Email not registered.'}, status=400)

            # Fetch image from Cloudinary
            image_data = None
            if images:
                img_response = requests.get(images[0])
                if img_response.status_code == 200:
                    image_data = img_response.content

            # Create LostItem record
            LostItem.objects.create(
                L_Description=description,
                L_PublishDate=date_now,
                L_information=l_info,
                U_ID=uid,
                L_Photo=image_data
            )

            return JsonResponse({'message': 'Lost item submitted successfully.'}, status=201)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)