from django.db import models

# Create your models here.
class Lomba(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

class Kategori(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)

class LombaKategori(models.Model):
    lomba_id = models.ForeignKey(Lomba, on_delete=models.CASCADE)
    kategori_id = models.ForeignKey(Kategori, on_delete=models.CASCADE)

class Jadwal(models.Model):
    lomba_id = models.ForeignKey(Lomba, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField(null=True)
