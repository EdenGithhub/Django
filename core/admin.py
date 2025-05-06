from django.contrib import admin
from .models import Culture

# Daftarkan model Culture agar bisa diakses di admin panel
admin.site.register(Culture)
