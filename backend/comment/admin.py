from django.contrib import admin

from .models import Comment, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    exclude = ()


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    exclude = ()
