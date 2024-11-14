from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignupForm

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pendaftaran berhasil!')
            return redirect('users:login')
        else:
            messages.error(request, 'Ada kesalahan pada pengisian form.')
    else:
        form = SignupForm()
    
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    return render(request, 'login.html')
