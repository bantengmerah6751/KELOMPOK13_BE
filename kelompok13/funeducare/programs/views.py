from django.shortcuts import render

# Create your views here.
def programs_view(request):
    return render(request,'programs/programs.html')