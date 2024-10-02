from django.urls import path

#project
from . import views


app_name='home'
urlpatterns = [
    path('',views.HomeView.as_view(), name='home'),
]
