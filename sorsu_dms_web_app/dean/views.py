from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

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

def test_db_connection(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        return HttpResponse("Database connection successful!")
    except Exception as e:
        return HttpResponse(f"Database connection failed: {e}")