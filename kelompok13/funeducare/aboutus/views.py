from django.shortcuts import render
from .models import Galeri

def aboutus_view(request):
    galeri_items = Galeri.objects.all()
    return render(request, 'aboutus/aboutus.html', {'galeri_items': galeri_items})
