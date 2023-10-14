# Generated by Django 4.1.2 on 2023-10-14 04:37

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PopularStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=150)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
