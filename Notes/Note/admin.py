from django.contrib import admin
from .models import *

# Register your models here.


class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'create_date', 'change_date', 'url', 'url_access')
    prepopulated_fields = {"url": ("title",)}


admin.site.register(Note, NoteAdmin)