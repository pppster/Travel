# Generated by Django 4.2.1 on 2023-06-23 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0014_remove_images_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='title',
            field=models.TextField(null=True),
        ),
    ]
