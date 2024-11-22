from django.urls import path
from pendaftaran import views

app_name = 'pendaftaran'
urlpatterns = [
    path('', views.pendaftaran, name='pendaftaran'),  # Form pendaftaran
    path('syarat/', views.syarat, name='syarat'),
]
