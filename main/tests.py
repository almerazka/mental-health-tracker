from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.utils import timezone
from .models import MoodEntry

class mainTest(TestCase):
    def test_main_url_is_exist(self): # tes untuk mengecek apakah path URL utama ('') dapat diakses
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self): # tes untuk mengecek apakah halaman utama di-render menggunakan template main.html
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self): # tes untuk mengecek apakah halaman yang tidak ada pada proyek Django memang benar-benar tidak ada dan akan memberikan kode respons 404 
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    def test_strong_mood_user(self): # tes untuk memeriksa logika kode, terutama pada saat menentukan apakah mood pengguna bisa dikatakan kuat dengan suatu nilai `mood_intensity_ yang tersimpan.
        now = timezone.now()
        mood = MoodEntry.objects.create(
          mood="LUMAYAN SENANG",
          time = now,
          feelings = "senang sih, cuman tadi baju aku basah kena hujan :(",
          mood_intensity = 8,
        )
        self.assertTrue(mood.is_mood_strong)