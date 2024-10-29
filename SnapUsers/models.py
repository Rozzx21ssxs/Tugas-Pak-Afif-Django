from django.db import models

# Create your models here.
class Pengguna(models.Model):
    username = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    role = models.CharField(max_length=10, choices=[('admin', 'admin'), ('peserta', 'peserta')])
    created_at = models.DateTimeField(auto_now_add=True, null=True)

class Juri(models.Model):
    user_id = models.OneToOneField(Pengguna, on_delete=models.CASCADE)
    bio = models.TextField(null=True)
