from django.urls import path
from .views import programs

app_name = 'programs'

urlpatterns = [
    path('', programs, name='programs'),

]