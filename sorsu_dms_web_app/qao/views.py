from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection


# Create your views here.
def home_page(request):
  return render(request,'qao/home_page.html')

def files_page(request):
  return render(request,'qao/files_page.html')

def profile_page(request):
  return render(request,'qao/profile_page.html')

def test_db_connection(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        return HttpResponse("Database connection successful!")
    except Exception as e:
        return HttpResponse(f"Database connection failed: {e}")
