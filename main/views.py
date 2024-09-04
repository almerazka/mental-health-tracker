from django.shortcuts import render

# Create your views here.
# Fungsi ini akan mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai.
def show_main(request):
    context = {
        'npm' : '2306241745',
        'name': 'Muhammad Almerazka Yocendra',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)

# request: Ini adalah objek permintaan HTTP yang dikirim oleh pengguna.
# main.html: Ini adalah nama berkas template yang akan digunakan untuk me-render tampilan.
# context: Ini adalah dictionary yang berisi data yang akan diteruskan ke tampilan untuk digunakan dalam penampilan dinamis.