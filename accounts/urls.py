from django.urls import path

#locals
from . import views

app_name='accounts'

urlpatterns = [
    path('register/',views.UserRegisterView.as_view(),name='user_register'),
    path('verify/',views.UserRegisterVerifyCode.as_view(),name='verify_code'),
]
