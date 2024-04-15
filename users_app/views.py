from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login
from .forms import CustomRegistrationForm
from .models import UserProfile

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)

            try:
                user_profile = UserProfile.objects.get(user=user)
                user_role = user_profile.role  
            except UserProfile.DoesNotExist:
                user_role = 'default_role'  

            
            request.session['user_role'] = user_role

            return redirect('home')  
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')  


def register(request):
    if request.method == "POST":
        register_form = CustomRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "New user account created") 
            return redirect('index')  
        else:
            print(register_form.errors)  
    else:
        register_form = CustomRegistrationForm()
    
    return render(request, 'register.html', {'register_form': register_form})

