from django.contrib import admin
from .models import Book, Like, Download
from unfold.admin import ModelAdmin

@admin.register(Book)
class BookAdmin(ModelAdmin):
    list_display = ("title", "author", "likes_count", "downloads_count", "daraja", "created_at")
    search_fields = ("title", "author")

@admin.register(Like)
class LikeAdmin(ModelAdmin):
    list_display = ("user", "book", "created_at")
    search_fields = ("user__username", "book__title")

@admin.register(Download)
class DownloadAdmin(ModelAdmin):
    list_display = ("user", "book", "created_at")
    search_fields = ("user__username", "book__title")