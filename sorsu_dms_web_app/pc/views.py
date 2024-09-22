from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

# Create your views here.

def Home(request):
  return render(request,'pc/Home.html')


def Create_Submission(request):
  return render(request,'pc/Create_Submission.html')


def Faculty_Files(request):
  return render(request,'pc/Faculty_Files.html')


def My_Profile(request):
  return render(request,'pc/My_Profile.html')

def test_db_connection(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        return HttpResponse("Database connection successful!")
    except Exception as e:
        return HttpResponse(f"Database connection failed: {e}")