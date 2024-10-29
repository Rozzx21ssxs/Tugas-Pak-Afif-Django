from django.db import models

from LensGallery.models import Foto
from SnapUsers.models import Juri, Pengguna

# Create your models here.
class Nilai(models.Model):
    photo_id = models.ForeignKey(Foto, on_delete=models.CASCADE)
    judge_id = models.ForeignKey(Juri, on_delete=models.CASCADE)
    score = models.IntegerField(null=True)
    comment = models.TextField(null=True)
    scoring_date = models.DateTimeField(auto_now_add=True, null=True)

class Komentar(models.Model):
    photo_id = models.ForeignKey(Foto, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Pengguna, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
