from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings 
from django.core.validators import MinLengthValidator, MaxLengthValidator

class CustomUser(AbstractUser):
    # Pilihan untuk jenis kelamin
    GENDER_CHOICES = [
        ('L', 'Pria'),
        ('P', 'Wanita'),
    ]

    # Menambahkan field untuk gender
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True,  # Jika tidak diisi, akan dianggap kosong
        null=True,   # Menyimpan nilai null jika tidak diisi
    )

    # Field tambahan
    birth_date = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    alamat = models.CharField(max_length=255, null=True, blank=True)
    no_telp = models.CharField(max_length=12, null=True, blank=True)

    def __str__(self):
        return self.username
    
class Anak(models.Model):
    JENIS_KELAMIN_CHOICES = [
        ('L', 'Laki-laki'),
        ('P', 'Perempuan')
    ]

    nama = models.CharField(
        max_length=100, 
        validators=[
            MinLengthValidator(2, "Nama minimal 2 karakter"),
            MaxLengthValidator(100, "Nama maksimal 100 karakter")
        ]
    )
    
    # Gunakan settings.AUTH_USER_MODEL
    ortu = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='anak'
    )
    
    tanggal_lahir = models.DateField()
    jenis_kelamin = models.CharField(
        max_length=1, 
        choices=JENIS_KELAMIN_CHOICES
    )
    
    # Tambahkan informasi tambahan
    alamat = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.nama} ({self.get_jenis_kelamin_display()})"
    
    def umur(self):
        from datetime import date
        today = date.today()
        return today.year - self.tanggal_lahir.year - (
            (today.month, today.day) < (self.tanggal_lahir.month, self.tanggal_lahir.day)
        )

class KegiatanAnak(models.Model):
    JENIS_KEGIATAN = [
        ('makan', 'Makan'),
        ('bermain', 'Bermain'),
        ('tidur', 'Tidur'),
        ('belajar', 'Belajar'),
        ('olahraga', 'Olahraga')
    ]

    STATUS_KEGIATAN = [
        ('mulai', 'Dimulai'),
        ('selesai', 'Selesai'),
        ('tertunda', 'Tertunda')
    ]

    anak = models.ForeignKey(
        Anak, 
        on_delete=models.CASCADE,
        related_name='kegiatan'
    )
    
    jenis = models.CharField(
        max_length=20, 
        choices=JENIS_KEGIATAN
    )
    
    deskripsi = models.TextField(
        blank=True, 
        null=True
    )
    
    waktu = models.DateTimeField()
    
    durasi = models.IntegerField(
        help_text="Durasi dalam menit",
        validators=[
            MinLengthValidator(1, "Durasi minimal 1 menit"),
        ]
    )
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_KEGIATAN,
        default='mulai'
    )
    
    catatan_tambahan = models.TextField(
        blank=True, 
        null=True, 
        help_text="Catatan tambahan tentang kegiatan"
    )
    
    class Meta:
        ordering = ['-waktu']
        verbose_name_plural = "Kegiatan Anak"

    def __str__(self):
        return f"{self.anak.nama} - {self.jenis} - {self.waktu}"
    
    def is_selesai(self):
        return self.status == 'selesai'
