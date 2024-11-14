from django.shortcuts import render

# Create your views here.

#? Membuat class form
from django import forms

""" Perlu di garis bawahi kalau untuk buat kelas form itu sama kayak models """
class ProgramsCompetitionForm(forms.Form):
  child_name = forms.CharField()
  parent_name = forms.CharField()
  parent_email = forms.EmailField()
  parent_phone = forms.CharField()


def programs(request):
  competition_form = ProgramsCompetitionForm()
  context = {
    'Judul': 'Our Programs',
    'competition_form': competition_form,
  }
  if request.method == "POST":
    print('ini POST')
    print(request.POST['child_name'])
    print(request.POST['parent_name'])
    print(request.POST['parent_email'])
    print(request.POST['parent_phone'])
  else:
    print('ini GET')
  return render(request, 'programs/programs.html', context)