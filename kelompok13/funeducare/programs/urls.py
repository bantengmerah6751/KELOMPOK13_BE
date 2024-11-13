from django.urls import path
from . import views

app_name = 'programs'
urlpatterns = [
    path('', views.programs_view, name='programs'),
]