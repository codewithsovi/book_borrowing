from django.db import models
from books.models import Book

# Create your models here.
class Peminjaman (models.Model):
    # menggunakan list tuple untuk pilihan status peminjaman
    STATUS_CHOICES = [
        ('dipinjam', 'Dipinjam'),
        ('dikembalikan', 'Dikembalikan'),
    ]

    nama_peminjam = models.CharField(max_length=255)
    nim = models.CharField(max_length=255)
    jurusan = models.CharField(max_length=255)
    no_telp = models.CharField(max_length=255, verbose_name="Nomor Telepon")
    buku = models.ForeignKey(Book, on_delete=models.CASCADE)
    tanggal_pinjam = models.DateField(auto_now_add=True)
    tanggal_kembali = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='dipinjam')

    def __str__(self):
        return f"{self.nama_peminjam} meminjam {self.buku.judul}"
    
    class Meta:
        verbose_name_plural = "Peminjaman"