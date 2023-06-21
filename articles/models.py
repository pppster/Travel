from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
    date_created = models.DateTimeField('Article Added',blank=True, auto_now_add=True)
    summary = models.TextField('Short Description', default="Kurzi")

class Image(models.Model):
    pass