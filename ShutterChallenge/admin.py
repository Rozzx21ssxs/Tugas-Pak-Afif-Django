from datetime import timezone
from django.contrib import admin

from LensGallery.models import DataExif, Foto
from PicRatings.models import Komentar, Nilai
from .models import Lomba, Kategori, LombaKategori, Jadwal
from SnapUsers.models import Pengguna, Juri
from ShutterChallenge.models import Lomba

# Register your models here.
class LombaAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'created_at')  # Menampilkan kolom yang diinginkan
    search_fields = ('title',)  # Pencarian berdasarkan title
    actions = ['mark_as_finished']  # Tambahkan aksi yang diinginkan

    def mark_as_finished(self, request, queryset):
        queryset.update(end_date=timezone.now())  # Contoh aksi: mengupdate end_date
        self.message_user(request, "Lomba telah ditandai selesai.")

class KategoriAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Menampilkan kolom name
    search_fields = ('name',)  # Pencarian berdasarkan name

class LombaKategoriAdmin(admin.ModelAdmin):
    list_display = ('lomba_id', 'kategori_id')  # Menampilkan kolom lomba dan kategori
    search_fields = ('lomba_id__title', 'kategori_id__name')  # Pencarian berdasarkan judul lomba dan nama kategori

class JadwalAdmin(admin.ModelAdmin):
    list_display = ('lomba_id', 'event_name', 'start_time', 'end_time')  # Menampilkan kolom yang diinginkan
    search_fields = ('event_name',)  # Pencarian berdasarkan event_name

class PenggunaAdmin(admin.ModelAdmin):
    list_display = ('username', 'role', 'created_at')  # Menampilkan kolom yang diinginkan
    search_fields = ('username',)  # Pencarian berdasarkan username

class JuriAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'bio')  # Menampilkan kolom yang diinginkan
    search_fields = ('bio',)  # Pencarian berdasarkan bio

class NilaiAdmin(admin.ModelAdmin):
    list_display = ('photo_id', 'judge_id', 'score', 'scoring_date')  # Menampilkan kolom yang diinginkan
    search_fields = ('judge_id__user_id__username',)  # Pencarian berdasarkan username juri

class KomentarAdmin(admin.ModelAdmin):
    list_display = ('photo_id', 'user_id', 'created_at')  # Menampilkan kolom yang diinginkan
    search_fields = ('user_id__username',)  # Pencarian berdasarkan username pengguna

class FotoAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'competition_id', 'upload_date')  # Menampilkan kolom yang diinginkan
    search_fields = ('caption',)  # Pencarian berdasarkan caption

class DataExifAdmin(admin.ModelAdmin):
    list_display = ('photo_id', 'camera_model', 'aperture', 'exposure_time', 'iso', 'focal_length', )  # Menampilkan kolom yang diinginkan
    search_fields = ('camera_model',)  # Pencarian berdasarkan camera_model

# Register your models here
admin.site.register(Kategori, KategoriAdmin)
admin.site.register(Lomba, LombaAdmin)
admin.site.register(LombaKategori, LombaKategoriAdmin)
admin.site.register(Jadwal, JadwalAdmin)
admin.site.register(Pengguna, PenggunaAdmin)
admin.site.register(Juri, JuriAdmin)
admin.site.register(Nilai, NilaiAdmin)
admin.site.register(Komentar, KomentarAdmin)
admin.site.register(Foto, FotoAdmin)
admin.site.register(DataExif, DataExifAdmin)