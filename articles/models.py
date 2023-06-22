from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
    date_created = models.DateTimeField('Article Added',blank=True, auto_now_add=True)
    summary = models.TextField('Short Description')


class Comment(models.Model):
    text = models.TextField()
    date_created = models.DateTimeField('Comment Added',blank=True, auto_now_add=True)
    creator = models.IntegerField("Comment Creator", blank=False, default=1)


class Image(models.Model):
    pass