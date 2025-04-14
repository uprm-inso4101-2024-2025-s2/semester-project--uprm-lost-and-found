from django.urls import path
from .views import homepage,signup, login_form, signup_form, found_item_page, lost_item_page, report_type_page, login_check

urlpatterns = [
    path('', homepage, name='homepage'),
    path('login/', login_form, name='login'),
    path('signup/', signup, name='signup'),
    path('signup/form/', signup_form, name='signup_form'),
    path('found/', found_item_page, name='found'),
    path('lost/', lost_item_page, name='lost'),
    path('report-type/', report_type_page, name='report_type'),
    path('login/check/', login_check, name='login_check'),
]
