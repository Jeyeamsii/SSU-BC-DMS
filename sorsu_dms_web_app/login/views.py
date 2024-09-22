from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.

def ResetPassword(request):
  return render(request,'login/ResetPassword.html')

def Log_In(request):
  return render(request,'login/Log_In.html')

def Forgot_Password(request):
  return render(request,'login/Forgot_password.html')

def Applied_NewPass(request):
  return render(request,'login/Applied_NewPass.html')

def login_view(request):
    if request.method == 'POST':
        # Get the data from the HTML form
        username = request.POST.get('username')
        password = request.POST.get ('password')

        # Manually check if fields are not empty
        if username and password:
            # Authenticate user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                
                # Redirect based on user group
                if user.groups.filter(name='Dean').exists():
                    return redirect('home')
                elif user.groups.filter(name='Program Chair').exists():
                    return redirect('Homepage')
                elif user.groups.filter(name='Quality Assurance Officer').exists():
                    return redirect('home_page')
                elif user.groups.filter(name='Faculty').exists():
                    return redirect('homepage')
                else:
                    # Redirect to default page if no group matches
                    return redirect('default_page')
            else:
                # Handle invalid credentials
                error_message = 'Invalid username or password'
        else:
            # Handle case where fields are empty
            error_message = 'Both username and password are required'
        
        # Render the form with the error message
        return render(request, 'login/Log_In.html', {'error_message': error_message})

    # If request is GET, render the form without any error message
    return render(request, 'login/Log_In.html')