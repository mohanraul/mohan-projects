from django.contrib import admin
from movieapp.models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display=['rdate','moviename','hero','heroine','rating']

# Register your models here.
admin.site.register(Movie,MovieAdmin)
