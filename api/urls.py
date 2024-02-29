from django.urls import path, include

urlpatterns = [
    path('acara/', include('acara.urls')),
    path('mahasiswa/', include('mahasiswa.urls')),
    path('bidang/', include('organisasi.urls')),
    path('kelompok/', include('kelompok.urls')),
]
