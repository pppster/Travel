# Generated by Django 4.2.1 on 2023-06-22 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_comment_alter_article_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Comment Added'),
        ),
    ]
