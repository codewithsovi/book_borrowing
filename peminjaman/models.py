from django.db import models

# Create your models here.
class Peminjaman(models.Model):
    nama_peminjam = models.CharField(max_length=100)
    nim_peminjam = models.CharField(max_length=20)
    telp_peminjam = models.CharField(max_length=20)
    jurusan = models.CharField(max_length=100)
    tanggal_pinjam = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nama_peminjam}"


class DetailPeminjaman(models.Model):
    peminjaman = models.ForeignKey(Peminjaman, on_delete=models.CASCADE, related_name='details')
    judul_buku = models.CharField(max_length=255)
    kode_buku = models.CharField(max_length=255)
    tanggal_wajib_kembali = models.DateField()
    status = models.CharField(max_length=20, default='Dipinjam')

    def __str__(self):
        return f"{self.judul_buku} - {self.status}"