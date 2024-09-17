from django.shortcuts import render

# Create your views here.

def ResetPassword(request):
  return render(request,'login/ResetPassword.html')

def Log_In(request):
  return render(request,'login/Log_In.html')

def Forgot_Password(request):
  return render(request,'login/Forgot_password.html')

def Applied_NewPass(request):
  return render(request,'login/Applied_NewPass.html')