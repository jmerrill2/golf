from django.contrib import admin

from .models import Volume, Book, Chapter, Verse


class BookInline(admin.TabularInline):
    model = Book
    readonly_fields = ('name', )
    can_delete=False
    extra = 0


class ChapterInline(admin.TabularInline):
    model = Chapter
    readonly_fields = ('number', 'book')
    can_delete=False
    extra = 0


class VerseInline(admin.TabularInline):
    model = Verse
    readonly_fields = ('number', 'chapter', 'text')
    can_delete=False
    extra = 0


class VolumeAdmin(admin.ModelAdmin):
    model = Volume
    inlines = (BookInline, )


class BookAdmin(admin.ModelAdmin):
    model = Book
    inlines = (ChapterInline, )


class ChapterAdmin(admin.ModelAdmin):
    model = Chapter
    inlines = (VerseInline, )


admin.site.register(Volume, VolumeAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Verse)
