# Generated by Django 4.2.1 on 2023-06-23 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_images'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Images',
        ),
    ]