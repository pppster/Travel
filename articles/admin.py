from django.contrib import admin
from .models import Article, Comment, Images

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title', 'content']

class ImageAdmin(admin.ModelAdmin):
    list_display=['file']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Images, ImageAdmin)
admin.site.register(Comment)


