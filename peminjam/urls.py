from django.urls import path
# Import dari folder views manual yang kita buat kemarin
from .views import dashboard_views, peminjaman_views

urlpatterns = [
    path('dashboard/', dashboard_views.halaman_dashboard, name='dashboard_admin'),
    # path('peminjaman/', peminjaman_views.halaman_peminjaman, name='daftar_transaksi'),
]