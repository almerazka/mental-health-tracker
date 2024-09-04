from django.db import models

# kelas dasar
class MoodEntry(models.Model): # nama model
    # atribut atau field pada model
    mood = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    feelings = models.TextField()
    mood_intensity = models.IntegerField()

    @property # decorator untuk menambahkan atribut read-only
    def is_mood_strong(self):
        return self.mood_intensity > 5