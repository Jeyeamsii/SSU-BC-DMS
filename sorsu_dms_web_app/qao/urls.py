from django.urls import path
from . import views

urlpatterns = [
    path('home_page/', views.home_page, name='home_page'),
    path('files_page/', views.files_page, name='files_page'),
    path('profile_page/', views.profile_page, name='profile_page'),
]