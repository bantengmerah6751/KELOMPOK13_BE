from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import CustomUser
from django_recaptcha.fields import ReCaptchaField
from django.core.validators import RegexValidator
class SignupForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        label="Nama Depan",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan Nama Depan '})
    )
    last_name = forms.CharField(
        required=True,
        label="Nama Belakang",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan Nama Belakang '})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan Email Anda'})
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan Password '})
    )
    password2 = forms.CharField(
        label="Verifikasi Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan Ulang Password '})
    )

    class Meta:
        model = get_user_model()  # Use the custom user model here
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan Username Anda'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Email sudah digunakan oleh pengguna lain.")
        return email

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    captcha = ReCaptchaField()
    
class ChangePasswordUserForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password','new_password1','new_password2']
        
        
class UserUpdateForm(forms.Form):
    username = forms.CharField(max_length=150, label='Username')
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    profile_image = forms.ImageField(required=False, label='Profile Image')
    alamat = forms.CharField(max_length=255, required=False, label='Alamat')  # Address field
    gender_choices = [('L', 'Laki-laki'), ('P', 'Perempuan')]  # Gender options
    gender = forms.ChoiceField(choices=gender_choices, required=False, label='Jenis Kelamin')
    no_telp = forms.CharField(
    max_length=12, 
    required=False, 
    label='No Telp', 
    validators=[RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Nomor telepon tidak valid.")]
   
)
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # Ensure user is passed for validation
        super().__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data['username']
        # Check if username already exists, excluding the current user
        if CustomUser.objects.filter(username=username).exclude(id=self.user.id).exists():
            raise forms.ValidationError("Username sudah terdaftar! Pilih username lain.")
        return username
