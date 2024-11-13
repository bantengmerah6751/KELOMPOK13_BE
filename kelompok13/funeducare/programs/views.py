from django.shortcuts import render

# Create your views here.
def programs(request):
  context = {
    'Judul': 'Our Programs'
  }
  return render(request, 'programs/programs.html', context)
