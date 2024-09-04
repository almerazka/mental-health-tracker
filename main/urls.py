from django.urls import path
from main.views import show_main
# Berkas urls.py pada aplikasi mengatur rute URL spesifik untuk fitur-fitur dalam aplikasi tersebut.
app_name = 'main'

urlpatterns = [ #mengatur rute URL yang terkait dengan aplikasi main
    path('', show_main, name='show_main'),
]