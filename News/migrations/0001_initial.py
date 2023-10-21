# Generated by Django 4.1.2 on 2023-10-21 05:16

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UZFI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_category', models.CharField(max_length=255)),
                ('new_category_uz', models.CharField(max_length=255, null=True)),
                ('new_category_en', models.CharField(max_length=255, null=True)),
                ('new_category_ru', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PopularStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=150)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('img', models.ImageField(upload_to='img')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vedio_New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_uz', models.CharField(max_length=255, null=True)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('title_ru', models.CharField(max_length=255, null=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('views', models.IntegerField(default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='News_Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_uz', models.CharField(max_length=255, null=True)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('title_ru', models.CharField(max_length=255, null=True)),
                ('img', models.ImageField(upload_to='img/')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('body_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('body_en', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('body_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('views', models.IntegerField(default=0)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now_add=True)),
                ('category', models.ManyToManyField(to='News.newscategory')),
                ('dekan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='UZFI.dekan')),
                ('kafedramanager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='UZFI.kafedramanager')),
                ('leadership', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='UZFI.leadership')),
            ],
        ),
    ]
