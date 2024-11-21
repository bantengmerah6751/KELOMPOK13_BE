from django.shortcuts import render
from .forms import ProgramsCompetitionForm
from datetime import date
# import models forms competition
from .models import ProgramsCompetitionModel
from .models import (
   ParentingSeminarModel,
   CookingClassModel,
   ChildrenExhibitionModel,
)

# Create your views here.

def programs(request):
  #queryset ORM-nya
  participant = ProgramsCompetitionModel.objects.all()
  programs_competitions_form =  ProgramsCompetitionForm(request.POST)

  #event program lainnya 
  parenting_seminar = ParentingSeminarModel.objects.all().order_by('date')
  cooking_class = CookingClassModel.objects.all().order_by('date')
  exhibition = ChildrenExhibitionModel.objects.all().order_by('date')

  context = {
    'Judul': 'Our Programs',
    'f_competition' : programs_competitions_form,
    'participants' : participant,

    #context event program lainnya
    'parenting_seminar' : parenting_seminar,
    'cooking_class' : cooking_class,
    'exhibition' : exhibition,
  }

  if request.method == 'POST':
    try:
        # Gabungkan tgl_lahir dari input form
        year = request.POST.get('tgl_lahir_year')
        month = request.POST.get('tgl_lahir_month')
        day = request.POST.get('tgl_lahir_day')
        tgl_lahir = date(int(year), int(month), int(day)) if year and month and day else None
    except ValueError:
        tgl_lahir = None  # Jika data tidak valid, set None
    
    # Ambil dan olah field lainnya
    nama = request.POST.get('nama')
    email = request.POST.get('email')
    jenkel = request.POST.get('jenkel')
    pesan = request.POST.get('pesan')
    agree = True if request.POST.get('agree') == "on" else False  # Konversi "on" ke True/False

    # Buat objek di database
    ProgramsCompetitionModel.objects.create(
        nama=nama,
        email=email,
        jenkel=jenkel,
        tgl_lahir=tgl_lahir,
        pesan=pesan,
        agree=agree
    )
  
  return render(request, 'programs/programs.html', context)