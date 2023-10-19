# Generated by Django 4.1.2 on 2023-10-19 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UZFI', '0001_initial'),
        ('News', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news_content',
            name='dekan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='UZFI.dekan'),
        ),
        migrations.AddField(
            model_name='news_content',
            name='yangiliklar',
            field=models.ManyToManyField(to='News.newscategory'),
        ),
    ]
