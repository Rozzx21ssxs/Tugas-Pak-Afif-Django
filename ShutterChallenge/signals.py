from django.db.models.signals import post_save
from django.dispatch import receiver
from LensGallery.models import Foto, DataExif
from .utils import extract_exif  # Pastikan fungsi extract_exif ada di utils.py
from fractions import Fraction


@receiver(post_save, sender=Foto)
def create_data_exif(sender, instance, created, **kwargs):
    if created:
        # Dapatkan path file dari instance foto
        file_path = instance.file_upload.path

        # Ekstrak data EXIF
        exif_data = extract_exif(file_path)

        # Buat instance DataExif dengan data yang diekstrak
        DataExif.objects.create(
            photo_id=instance,
            camera_model=exif_data.get("Model"),
            aperture=exif_data.get("ApertureValue") or exif_data.get("FNumber"),
            exposure_time=exif_data.get("ExposureTime"),
            iso=exif_data.get("ISOSpeedRatings"),
            focal_length=exif_data.get("FocalLength")
        )