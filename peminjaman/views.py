from django.shortcuts import render
from django.http import HttpResponse
from peminjaman.models import Peminjaman

# Create your views here.
def dashboard(request):
    peminjaman = Peminjaman.objects.all()
    context = {
        'peminjaman': peminjaman,
    }
    return render(request, 'admin/dashboard.html', context)

def peminjaman_list(request):
    peminjaman = Peminjaman.objects.all()
    context = {
        'peminjaman': peminjaman,
    }
    return render(request, 'admin/peminjaman/index.html', context)
