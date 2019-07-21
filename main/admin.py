from django.contrib import admin
from .models import Song
from tinymce.widgets import TinyMCE
from django.db import models

class SongAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {'fields': ["name", "song_uploaded_on"]}),
        ("Content", {"fields": ["description"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

admin.site.register(Song, SongAdmin)