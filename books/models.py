from django.db import models
from categories.models import Category

# Create your models here.
class Book(models.Model):
    judul = models.CharField(max_length=255)
    penulis = models.CharField(max_length=255)
    sinopsis = models.TextField(blank=True, null=True)
    tanggal_terbit = models.DateField()
    total_stok = models.PositiveIntegerField(default=1, verbose_name="Total Buku Fisik")
    buku_display = models.PositiveIntegerField(default=1, verbose_name="Jumlah Buku Display")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.judul
