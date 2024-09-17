from django.shortcuts import render

# Create your views here.
def home_page(request):
  return render(request,'qao/home_page.html')

def files_page(request):
  return render(request,'qao/files_page.html')

def profile_page(request):
  return render(request,'qao/profile_page.html')