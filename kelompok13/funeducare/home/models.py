from django.db import models 

# Create your models here.
class Fasilitas(models.Model):
    judul = models.CharField(max_length=100)
    deskripsi = models.TextField()
    foto = models.FileField()
    
    def __str__(self):
        return f"{self.id} - {self.judul}"