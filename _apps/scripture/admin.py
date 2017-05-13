from django.contrib import admin

from .models import Volume, Book, Chapter, Verse

admin.site.register(Volume)
admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(Verse)
