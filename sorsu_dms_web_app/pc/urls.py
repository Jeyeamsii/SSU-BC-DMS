from django.urls import path
from . import views
from .views import test_db_connection

urlpatterns = [
    path('Home/', views.Home, name='Home'),
    path('My_Profile/', views.My_Profile, name='My_Profile'),
    path('Create_Submission,/', views.Create_Submission, name='Create_Submission'),
    path('Faculty_Files/', views.Faculty_Files, name='Faculty_Files'),
    path('test-db/', test_db_connection),
]