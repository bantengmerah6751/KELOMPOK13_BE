from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .forms import SignupForm
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

@login_required
def user_logout(request):
    logout(request)
    next_url = request.GET.get('next', '/')  # Jika ada next di URL, arahkan ke halaman tersebut
    return redirect(next_url)  

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pendaftaran berhasil!')
            return redirect('users:login')
        else:
            messages.error(request, 'Ada kesalahan saat pengisian form.')
    else:
        form = SignupForm()
    
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    form = LoginForm()  
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid(): 
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Login berhasil! Selamat datang di FunEduCare.')
                    return redirect('home:home')  
                else:
                    messages.error(request, 'Akun Anda tidak aktif. Silakan hubungi admin.')
                    return redirect('users:login')
            else:
                messages.error(request, 'Username atau password salah.')
    return render(request, 'login.html', {'form': form})
    
def profile_view(request):
    return render(request, 'profile.html')