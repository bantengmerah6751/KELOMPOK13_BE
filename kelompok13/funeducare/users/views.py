from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import  login,logout
from .forms import SignupForm,LoginForm,ChangePasswordUserForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import KegiatanAnak, Anak
from django.http import JsonResponse

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
            messages.success(request, 'Pendaftaran berhasil ! Silakan login.')
            return redirect('users:login')  # Redirect to login page after successful signup
        else:
            messages.error(request, 'Ada kesalahan saat pengisian form.')
    else:
        form = SignupForm()
    
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)  
        if form.is_valid():  # form valid ( validasi captcha)
            user = form.get_user()  #  user auth get
            login(request, user)  # Login user ke session
            user = request.user.username
            messages.success(request, f'Login berhasil ! Selamat datang {user}') 
            return redirect('home:home')  # Redirect ke halaman home setelah login berhasil
        else:
            print(form.errors)  
            if form.errors.get('captcha'):  # Jika ada error di captcha
                messages.error(request, 'reCAPTCHA tidak valid, silakan coba lagi.')
            else:
                messages.error(request, 'Login gagal ! Username atau password salah.')
            return redirect('users:login')  #  form tidak valid, redirect ke halaman login
    else:
        form = LoginForm()  # GET, tampilkan form login kosong
    
    return render(request, 'login.html', {'form': form})

def change_password(request):
    form = ChangePasswordUserForm(request.user, request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home:home')
        else:
            return redirect('users:change_password')
    else:
        form = ChangePasswordUserForm(request.user)
    
    context={
        'judul':'Change password',
        'form' : form,
    }
    return render(request,'change_password.html', context)

@login_required
def update_account(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, user=request.user)
        
        if form.is_valid():
            # Get cleaned data from the form
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            alamat = form.cleaned_data.get('alamat', request.user.alamat)  
            no_telp = form.cleaned_data.get('no_telp', request.user.no_telp)  
            gender = form.cleaned_data.get('gender', request.user.gender) 

            changes_made = False

            if request.user.username != username:
                request.user.username = username
                changes_made = True
            if request.user.first_name != first_name:
                request.user.first_name = first_name
                changes_made = True
            if request.user.last_name != last_name:
                request.user.last_name = last_name
                changes_made = True
            if request.user.alamat != alamat:
                request.user.alamat = alamat
                changes_made = True
            if request.user.no_telp != no_telp:
                request.user.no_telp = no_telp
                changes_made = True
            if request.user.gender != gender:
                request.user.gender = gender
                changes_made = True

        
            if form.cleaned_data.get('profile_image'):
                if request.user.profile_image != form.cleaned_data['profile_image']:
                    request.user.profile_image = form.cleaned_data['profile_image']
                    changes_made = True

            if 'delete_image' in request.POST and request.POST['delete_image'] == 'on':
                if request.user.profile_image:
                    request.user.profile_image = None
                    changes_made = True

            # If there were any changes, save the user
            if changes_made:
                request.user.save()
                messages.success(request, "Akun berhasil diperbarui")
            else:
                # If no changes, inform the user
                messages.info(request, "Tidak ada perubahan yang dilakukan.")

            return redirect('users:pengaturanakun')
        else:
            # If form is invalid, show error message
            messages.error(request, "Username sudah digunakan! Silakan coba lagi.")
    else:
        # If the method is GET, populate the form with the current user data
        form = UserUpdateForm(initial={
            'username': request.user.username,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'alamat': request.user.alamat,  # Assuming these fields are in the model
            'no_telp': request.user.no_telp,
            'gender': request.user.gender,  # Adding gender to pre-fill the form
        }, user=request.user)

    return render(request, 'pengaturan_akun.html', {'form': form})

@login_required
def dashboard_kegiatan(request):
    # Dapatkan anak yang terkait dengan orang tua yang login
    anak = Anak.objects.filter(ortu=request.user)
    
    # Ambil kegiatan untuk anak-anak tersebut
    kegiatan = KegiatanAnak.objects.filter(anak__in=anak)
    
    context = {
        'kegiatan': kegiatan
    }
    return render(request, 'riwayat_kegiatan.html', context)

def get_kegiatan_api(request):
    # API untuk mendapatkan data kegiatan dalam format JSON
    anak = Anak.objects.filter(ortu=request.user)
    kegiatan = KegiatanAnak.objects.filter(anak__in=anak)
    
    data = [{
        'id': k.id,
        'nama_anak': k.anak.nama,
        'jenis': k.jenis,
        'deskripsi': k.deskripsi,
        'waktu': k.waktu.strftime('%H:%M'),
        'durasi': k.durasi
    } for k in kegiatan]
    
    return JsonResponse(data, safe=False)


def profile_view(request): 
    return render(request,'profil_anak.html')
def program_aktif(request):
    return render(request,'program_aktif.html')
def riwayat_kegiatan(request):
    return render(request,'riwayat_kegiatan.html')
def laporan_perkembangan(request):
    return render(request,'laporan_perkembangan.html')
def pembayaran(request):
    return render(request,'riwayat_pembayaran.html')
