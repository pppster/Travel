# Generated by Django 4.2.1 on 2023-06-23 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_alter_article_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='')),
                ('title', models.TextField()),
            ],
        ),
    ]
