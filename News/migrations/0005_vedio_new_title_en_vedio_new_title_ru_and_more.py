# Generated by Django 4.1.2 on 2023-09-28 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0004_alter_vedio_new_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='vedio_new',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='vedio_new',
            name='title_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='vedio_new',
            name='title_uz',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
