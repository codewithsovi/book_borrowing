from django.db import models

# Create your models here.
class Category(models.Model):
    nama = models.CharField(max_length=255)
    deskripsi = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nama