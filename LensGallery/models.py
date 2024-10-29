from django.db import models # type: ignore
from SnapUsers.models import Pengguna  # Pastikan import Pengguna dari app terkait
from ShutterChallenge.models import Lomba


class Foto(models.Model):
    user_id = models.ForeignKey(Pengguna, on_delete=models.CASCADE)
    competition_id = models.ForeignKey(Lomba, on_delete=models.CASCADE)
    file_upload = models.FileField(upload_to='uploads/photos/', null=True, blank=True)
    caption = models.TextField(null=True)
    upload_date = models.DateTimeField(auto_now_add=True, null=True)

class DataExif(models.Model):
    photo_id = models.ForeignKey(Foto, on_delete=models.CASCADE)
    camera_model = models.CharField(max_length=255, null=True)
    aperture = models.CharField(max_length=20, null=True)
    exposure_time = models.CharField(max_length=20, null=True)
    iso = models.CharField(max_length=10, null=True)
    focal_length = models.CharField(max_length=20, null=True)
