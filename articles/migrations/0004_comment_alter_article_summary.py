# Generated by Django 4.2.1 on 2023-06-22 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_image_article_date_created_article_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Article Added')),
                ('creator', models.IntegerField(default=1, verbose_name='Comment Creator')),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='summary',
            field=models.TextField(verbose_name='Short Description'),
        ),
    ]
