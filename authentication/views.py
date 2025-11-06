from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    return render(request=request, template_name='index.html')

def login_user(request):
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

def logout_user(request):
    logout(request=request)
    return redirect(to='/')