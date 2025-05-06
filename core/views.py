from .models import Culture
from django.shortcuts import render, redirect
from .forms import CultureForm


def home(request):
    return render(request, 'core/home.html')


def explore(request):
    cultures = Culture.objects.all()
    return render(request, 'core/explore.html', {'cultures': cultures})


def submit_culture(request):
    if request.method == 'POST':
        # Jangan lupa tambahkan request.FILES untuk upload gambar
        form = CultureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect ke halaman explore setelah berhasil
            return redirect('explore')
    else:
        form = CultureForm()
    return render(request, 'core/submit_culture.html', {'form': form})


def about(request):
    return render(request, 'core/about.html')
