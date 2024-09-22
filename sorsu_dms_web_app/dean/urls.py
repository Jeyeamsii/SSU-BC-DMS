from django.urls import path
from . import views
from .views import test_db_connection


urlpatterns = [
    path('archive/', views.archive, name='archive'),
    path('home/', views.home, name='home'),
    path('files/', views.files, name='files'),
    path('profilePage/', views.profilePage, name='profilePage'),
    path('userManagement/', views.userManagement, name='userManagement'),
    path('test-db/', test_db_connection),
]