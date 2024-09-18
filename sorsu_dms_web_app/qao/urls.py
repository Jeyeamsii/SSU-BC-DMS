from django.urls import path
from . import views
from .views import test_db_connection

urlpatterns = [
    path('home_page/', views.home_page, name='home_page'),
    path('files_page/', views.files_page, name='files_page'),
    path('profile_page/', views.profile_page, name='profile_page'),
    path('test-db/', test_db_connection),
]