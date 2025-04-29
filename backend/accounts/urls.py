from django.urls import path
from .views import homepage, signup, login_form, signup_form, found_item_page, lost_item_page, report_type_page, \
    login_check, submit_lost_item, logout_view, my_cases_page, submit_found_item

urlpatterns = [
    path('', homepage, name='homepage'),
    path('login/', login_form, name='login'),
    path('signup/', signup, name='signup'),
    path('signup/form/', signup_form, name='signup_form'),
    path('found/', found_item_page, name='found'),
    path('lost/', lost_item_page, name='lost'),
    path('report-type/', report_type_page, name='report_type'),
    path('my_cases/', my_cases_page, name='my_cases'),
    path('login/check/', login_check, name='login_check'),
    path('lost/submit/', submit_lost_item, name='submit_lost_item'),
    path('found/submit/', submit_found_item, name='submit_found_item'),
path('logout/', logout_view, name='logout'),

]
