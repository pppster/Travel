# Generated by Django 4.2.1 on 2023-06-23 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_fileupload'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='FileUpload',
        ),
    ]
