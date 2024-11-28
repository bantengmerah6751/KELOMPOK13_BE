from django.db import models

class Galeri(models.Model):
    nama = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='galeri_photos/', null=True, blank=True)
    deskripsi_singkat = models.TextField()
    deskripsi_detail = models.TextField()

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = "Galeri"
