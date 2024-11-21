from django.db import models

# Create your models here.
class ProgramsCompetitionModel(models.Model):
  #Disini kita akan menyimpan data dari forms ke model
  #Maka propertinya haruslah sama dengan di forms
  nama = models.CharField(max_length=25)
  email = models.EmailField()
  JENKEL_CHOICES = [
    ('l', 'Laki-Laki'),
    ('p', 'Perempuan')
  ]
  jenkel = models.CharField(
    max_length=1,
    choices=JENKEL_CHOICES,
    verbose_name="Jenis Kelamin"
  )
  tgl_lahir = models.DateField(verbose_name="Tanggal Lahir", null=False, blank=False)
  pesan = models.TextField()
  agree = models.BooleanField(
    verbose_name="Saya setuju untuk mengikuti lomba dan mengikuti syarat dan ketentuan yang berlaku",
    default=False
  )

  def __str__(self):
    return "%d %s" % (self.id, self.nama)
  
class ParentingSeminarModel(models.Model):
  date = models.DateField()
  title = models.CharField(max_length=200)
  speaker = models.CharField(max_length=100)

  TICKET_STATUS_CHOICES = [
    ('available', 'Tiket Tersedia'),
    ('limited', 'Tiket Hampir Habis'),
    ('sold_out', 'Tiket Habis Terjual')
  ]

  ticket_status = models.CharField(
    max_length=20,
    choices=TICKET_STATUS_CHOICES,
    default='available'
  )

  class Meta:
    ordering = ['date']
    verbose_name = 'Parenting Seminar'
    verbose_name_plural = 'Parenting Seminars'

  def __str__(self):
    return f"{self.date} - {self.title}"
  
class CookingClassModel(models.Model):
  date = models.DateField()
  title = models.CharField(max_length=200)
  instructor = models.CharField(max_length=100)

  TICKET_STATUS_CHOICES = [
    ('available', 'Tiket Tersedia'),
    ('limited', 'Tiket Hampir Habis'),
    ('sold_out', 'Tiket Habis Terjual')
  ]

  ticket_status = models.CharField(
    max_length=20,
    choices=TICKET_STATUS_CHOICES,
    default='available'
  )

  class Meta:
    ordering = ['date']
    verbose_name = 'Cooking Class'
    verbose_name_plural = 'Cooking Classes'

  def __str__(self):
    return f"{self.date} - {self.title}"

class ChildrenExhibitionModel(models.Model):
  date = models.DateField()
  title = models.CharField(max_length=200)
  description = models.TextField()

  REGISTRATION_STATUS_CHOICES = [
    ('open', 'Daftar Sekarang'),
    ('limited', 'Tempat Terbatas'),
    ('closed', 'Pendaftaran Tutup'),
  ]

  registration_status = models.CharField(
    max_length=20,
    choices=REGISTRATION_STATUS_CHOICES,
    default='open'
  )

  class Meta:
    ordering = ['date']
    verbose_name = 'Children Exhibition'
    verbose_name_plural = 'Children Exhibitions'
  
  def __str__(self):
    return f"{self.date} - {self.title}"