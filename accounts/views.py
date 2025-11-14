from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm

def login_user(request):
    if request.user.is_authenticated:
        return redirect(to='agenda')

    if request.POST:
        username = request.POST.get('username').strip()
        password = request.POST.get('password').strip()
        
        if not username or not password:
            messages.warning(request=request, message='Por favor, preencha todos os campos.')
            return redirect('login')
        
        user = authenticate(username=username, password=password)
        
        if user:
            login(request, user)
            next_url = request.GET.get('next', 'agenda')
            return redirect(to=next_url)
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
            return redirect(to='login')
    return render(request=request, template_name='login.html')

def create_user(request):
    # User creation
    if request.POST:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request=request, message='Conta criada com sucesso')
            return redirect(to='login')
    else:
        form = CustomUserCreationForm()
    return render(request=request, template_name='register.html', context={'form': form})

@login_required(login_url='login')
def profile_user(request):
    # Edit profile
    return render(request=request, template_name='profile.html')

def edit_profile(request):
    pass

def logout_user(request):
    logout(request=request)
    return redirect(to='/')