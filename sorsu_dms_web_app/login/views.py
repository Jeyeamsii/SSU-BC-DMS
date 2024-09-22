from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

def login_view(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(request, username=username, password=password)

      if user is not None:
        login(request, user)
        if user.groups.filter(name='Dean').exists():
          return redirect('home')
        elif user.groups.filter(name='Program Chair').exists():
          return redirect('Home')
        elif user.groups.filter(name='Quality Assurance Officer').exists():
          return redirect('home_page')
        elif user.groups.filter(name='Faculty').exists():
          return redirect('homepage')
      
      else:
        form.add_error(None, 'Invalid username or  password')

  else:
    form = LoginForm()


  return render(request, 'login/Login.html', {'form':form})    

@login_required
def home(request):
    return render(request, 'home.html', {'user': request.user})      