# Generated by Django 4.1.2 on 2023-09-27 17:19

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0003_vedio_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vedio_new',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
    ]
