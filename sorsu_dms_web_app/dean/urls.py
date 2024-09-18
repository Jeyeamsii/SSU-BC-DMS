from django.urls import path
from . import views


urlpatterns = [
    path('archive/', views.archive, name='archive'),
    path('home/', views.home, name='home'),
    path('files/', views.files, name='files'),
    path('profilePage/', views.profilePage, name='profilePage'),
    path('userManagement/', views.userManagement, name='userManagement'),
]