import uuid  # tambahkan baris ini di paling atas
from django.db import models
from django.contrib.auth.models import User

# kelas dasar
class MoodEntry(models.Model): # nama model
    # atribut atau field pada model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    mood = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    feelings = models.TextField()
    mood_intensity = models.IntegerField()

    @property # decorator untuk menambahkan atribut read-only
    def is_mood_strong(self):
        return self.mood_intensity > 5