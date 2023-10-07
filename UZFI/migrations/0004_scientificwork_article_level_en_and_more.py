# Generated by Django 4.1.2 on 2023-10-07 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UZFI', '0003_scientificwork_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='scientificwork',
            name='article_level_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='scientificwork',
            name='article_level_ru',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='scientificwork',
            name='article_level_uz',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='scientificwork',
            name='article_name_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='scientificwork',
            name='article_name_ru',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='scientificwork',
            name='article_name_uz',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='scientificwork',
            name='publication_date_en',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scientificwork',
            name='publication_date_ru',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scientificwork',
            name='publication_date_uz',
            field=models.DateField(blank=True, null=True),
        ),
    ]
