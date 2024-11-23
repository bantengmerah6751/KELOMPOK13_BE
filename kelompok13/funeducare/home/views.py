from django.shortcuts import render
from .models import Fasilitas

def home_view(request):
    fasilitas = Fasilitas.objects.all()[:3]  # Hanya mengambil 3 data pertama
    return render(request, 'home/index.html', {'Fasilitas': fasilitas})

def detail_fasilitas(request, fasilitas_id):
    dt = Fasilitas.objects.get(pk=fasilitas_id)
    all_fasilitas = Fasilitas.objects.all()
    return render(request, 'home/detail_fasilitas.html', {'detail': dt, 'all':all_fasilitas})

def fasilitas(request):
    all_fasilitas = Fasilitas.objects.all()
    return render(request, 'home/fasilitas.html', {'all':all_fasilitas})
