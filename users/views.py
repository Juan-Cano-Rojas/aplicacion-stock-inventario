from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


from .forms import LoginForm
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

def login_page(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
    context = {'form': forms}
    return render(request, 'users/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')

def register(request): 
    data = {
        'form': CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        
        if user_creation_form.is_valid():
            user_creation_form.save()
            
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.clean_data['password1'])
            login(request, user)
            return redirect('dashboard') 
        
    return render(request, 'users/register.html')
