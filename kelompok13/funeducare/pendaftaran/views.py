from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import BookingForm
from .models import Pendaftaran

def pendaftaran(request):
    if request.method == 'POST':
        form = BookingForm(request.POST, request.FILES)
        if form.is_valid():
            Pendaftaran.objects.create(
                nama_ortu=form.cleaned_data['nama_ortu'],
                email=form.cleaned_data['email'],
                nomor_wa=form.cleaned_data['nomor_wa'],
                alamat=form.cleaned_data['alamat'],
                ktp=request.FILES['ktp'],
                nama_anak=form.cleaned_data['nama_anak'],
                umur_anak=form.cleaned_data['umur_anak'],
                jenis_kelamin=form.cleaned_data['jenis_kelamin'],
                akta_kelahiran=request.FILES['akta_kelahiran'],
                program=form.cleaned_data['program']
            )
            return render(request, 'form_booking_success.html')
    else:
        form = BookingForm()

    context = {
        'form_booking': form,
    }
    return render(request, 'form_booking.html', context)

def syarat(request):
    return render(request, 'syarat.html')
def cara_mendaftar(request):
    return render(request, 'cara_mendaftar.html')
