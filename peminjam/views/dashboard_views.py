from django.shortcuts import render
from books.models import Book
from peminjam.models import Peminjaman 

def halaman_dashboard(request):
    total_buku = Book.objects.count()
    
    total_dipinjam = Peminjaman.objects.filter(status='dipinjam').count()
    
    peminjaman_kritis = Peminjaman.objects.filter(status='dipinjam').order_by('-tanggal_pinjam')[:5]

    # 4. Bungkus semua data ke dalam "Context" (Dictionary) untuk dilempar ke HTML
    context = {
        'total_buku': total_buku,
        'total_dipinjam': total_dipinjam,
        'peminjaman_kritis': peminjaman_kritis,
    }

    # 5. Render ke folder template admin sesuai struktur modular kamu
    return render(request, 'admin/dashboard.html', context)