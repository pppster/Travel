from django.db import models
import os

# Create your models here.
class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
    date_created = models.DateTimeField('Article Added',blank=True, auto_now_add=True)
    summary = models.TextField('Short Description')
    # image = models.ImageField(upload_to='images/', null=True, blank=True)
    


class Comment(models.Model):
    text = models.TextField()
    date_created = models.DateTimeField('Comment Added',blank=True, auto_now_add=True)
    creator = models.IntegerField("Comment Creator", blank=False, default=1)
    article = models.IntegerField("Article", blank=False, default=1)

class Images(models.Model):
    file = models.FileField(null=True, upload_to='images/')
    title = models.TextField(default='title')

    def filename(self):
        return os.path.basename(self.file.name)