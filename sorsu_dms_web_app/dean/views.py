from django.shortcuts import render

# Create your views here.
def archive(request):
  return render(request,'dean/archive.html')

def files(request):
  return render(request,'dean/files.html')

def home(request):
  return render(request,'dean/home.html')

def userManagement(request):
  return render(request,'dean/userManagement.html')

def profilePage(request):
  return render(request,'dean/profilePage.html')