# Generated by Django 4.1.2 on 2023-09-28 09:52

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News_Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('title_uz', models.CharField(max_length=255, null=True)),
                ('title_ru', models.CharField(max_length=255, null=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('body_en', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('body_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('body_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('views', models.IntegerField(default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_category', models.CharField(max_length=255)),
                ('new_category_en', models.CharField(max_length=255, null=True)),
                ('new_category_uz', models.CharField(max_length=255, null=True)),
                ('new_category_ru', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vedio_New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('title_uz', models.CharField(max_length=255, null=True)),
                ('title_ru', models.CharField(max_length=255, null=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('views', models.IntegerField(default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
