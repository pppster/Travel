# Generated by Django 4.2.1 on 2023-06-24 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0019_alter_images_article_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='article_id',
        ),
    ]