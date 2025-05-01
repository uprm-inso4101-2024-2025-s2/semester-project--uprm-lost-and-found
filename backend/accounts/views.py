from contextlib import nullcontext

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

# from .models import Location
from .models import LostItem, User
from .models import FoundItem, User
from datetime import datetime
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
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
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # redirect to login if user not logged in
    user = get_object_or_404(User, U_ID=user_id)
    lost_items = LostItem.objects.filter(U_ID=user_id).order_by('-L_PublishDate')
    found_items = FoundItem.objects.filter(U_ID=user_id).order_by('-F_PublishDate')
    return render(request, 'accounts/index.html', {'lost_items': lost_items, 'found_items': found_items})

def found_item_page(request):
    return render(request, 'accounts/founditem.html')

def lost_item_page(request):
    return render(request, 'accounts/lostitem.html')

def report_type_page(request):
    return render(request, 'accounts/report-type.html')

# def my_cases_page(request):
#     return render(request, 'accounts/my_cases.html')

# Log in handler
@csrf_exempt

def login_check(request):
        if request.method == 'POST':
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')

            try:
                user = User.objects.get(U_Email=email, U_Password=password)
                request.session['user_id'] = user.U_ID
                request.session['user_name'] = user.U_FullName

                # ✅ Include redirect URL
                return JsonResponse({
                    'message': f'Welcome, {user.U_FullName}',
                    'redirect': '/'
                }, status=200)

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
                L_information=comments,
                L_Location=location,
                U_ID=uid,
                L_Photo=image_data,
                L_Email=email,
            )

            return JsonResponse({'message': 'Lost item submitted successfully.'}, status=201)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)




@csrf_exempt
def submit_found_item(request):
    if request.method == 'POST':
        print(f"Request Body: {request.body.decode('utf-8')}")
        try:
            data = json.loads(request.body)
            description = data.get('description')
            location = data.get('foundLocation')
            additional_details = data.get('comments', '')
            comments = data.get('comments', '')
            email = data.get('contactEmail')

            images = data.get('images', [])

            # Build info
            f_info = f"{location} - {comments}"
            date_now = datetime.now().strftime("%Y-%m-%d")
            if not location:
                return JsonResponse({'error': 'Please specify where the item was found.'}, status=400)

            # Get user ID
            try:
                user = User.objects.get(U_Email=email)
                uid = user.U_ID
            except User.DoesNotExist:
                return JsonResponse({'error': 'Email not registered.'}, status=400)


            # Get loc for PID
            # try:
            #     location = Location.objects.get(P_Name=location)
            #     pid = location.P_ID
            # except Location.DoesNotExist:
            #     return JsonResponse({'error': f'Location "{location}" does not exist.'}, status=400)
            # Fetch image from Cloudinary
            image_data = None
            if images:
                img_response = requests.get(images[0])
                if img_response.status_code == 200:
                    image_data = img_response.content

            # Create FoundItem record
            FoundItem.objects.create(
                F_Description=description,
                F_PublishDate=date_now,
                F_PlaceFound=location,
                F_AdditionalDetails=additional_details,
                F_Photo=image_data,
                U_ID=uid,
                F_Email=email,

            )

            return JsonResponse({'message': 'Found item submitted successfully.'}, status=201)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)


@csrf_exempt
def my_cases_page(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # redirect to login if user not logged in

    user = get_object_or_404(User, U_ID=user_id)
    lost_items = LostItem.objects.filter(U_ID=user_id).order_by('-L_PublishDate')
    found_items = FoundItem.objects.filter(U_ID=user_id).order_by('-F_PublishDate')
    return render(request, 'accounts/my_cases.html', { 'user': user, 'lost_items': lost_items, 'found_items': found_items})



@csrf_exempt
def logout_view(request):
    request.session.flush()  # Clear all session data
    return redirect('login')

@csrf_exempt
def serve_lost_item_image(request, item_id):
    lost_item = get_object_or_404(LostItem, L_ID=item_id)
    if lost_item.L_Photo:
        return HttpResponse(lost_item.L_Photo, content_type='media/lost_items_photos')
    else:

        return HttpResponse(status=204)

def serve_found_item_image(request, item_id):
    found_item = get_object_or_404(FoundItem, F_ID=item_id)
    if found_item.F_Photo:
        return HttpResponse(found_item.F_Photo, content_type='media/lost_items_photos')
    else:
        return HttpResponse(status=204)


@require_POST
def delete_lost_item(request, item_id):
    lost_item = get_object_or_404(LostItem, L_ID=item_id, U_ID=request.session.get('user_id'))
    lost_item.delete()
    return redirect('my_cases')

@require_POST
def delete_found_item(request, item_id):
    found_item = get_object_or_404(FoundItem, F_ID=item_id, U_ID=request.session.get('user_id'))
    found_item.delete()
    return redirect('my_cases')