from django.shortcuts import render

# Create your views here.
def archive(request):
  return render(request,'admin/archive.html')