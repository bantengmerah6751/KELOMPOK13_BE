from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
app_name = 'users'
urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.profile_view, name='profile'),
    
]