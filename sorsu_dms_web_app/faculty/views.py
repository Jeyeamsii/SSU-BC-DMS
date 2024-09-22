from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

# Create your views here.

def homepage(request):
  return render(request,'faculty/homepage.html')


def submission_bin_page(request):
  return render(request,'faculty/submission_bin_page.html')


def my_portfolio_page(request):
  return render(request,'faculty/my_portfolio_page.html')


def profile_page(request):
  return render(request,'faculty/profile_page.html')

def test_db_connection(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        return HttpResponse("Database connection successful!")
    except Exception as e:
        return HttpResponse(f"Database connection failed: {e}")