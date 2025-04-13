from django.urls import path
from .views import signup, signup_form, login_form, login_check

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signup/form/', signup_form, name='signup_form'),
    path('login/', login_form, name='login_form'),
    path('login/check/', login_check, name='login_check'),
]
