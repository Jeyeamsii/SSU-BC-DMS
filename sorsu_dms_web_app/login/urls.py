from django.urls import path
from . import views

urlpatterns = [
    path('ResetPassword/', views.ResetPassword, name='ResestPassword'),
    path('Log_In/', views.Log_In, name='Log_In'),
    path('Forgot_Password/', views.Forgot_Password, name='Forgot_Password'),
    path('Applied_NewPass/', views.Applied_NewPass, name='Applied_NewPass'),
]