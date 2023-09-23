# Generated by Django 4.1.2 on 2023-09-23 05:07

import ckeditor.fields
import ckeditor_uploader.fields
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CentersDepartments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Charter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', ckeditor.fields.RichTextField()),
                ('title_en', ckeditor.fields.RichTextField(null=True)),
                ('title_uz', ckeditor.fields.RichTextField(null=True)),
                ('title_ru', ckeditor.fields.RichTextField(null=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('body_en', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('body_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('body_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Councils',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', ckeditor.fields.RichTextField()),
                ('title_en', ckeditor.fields.RichTextField(null=True)),
                ('title_uz', ckeditor.fields.RichTextField(null=True)),
                ('title_ru', ckeditor.fields.RichTextField(null=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('body_en', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('body_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('body_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.CharField(max_length=100)),
                ('document_type_en', models.CharField(max_length=100, null=True)),
                ('document_type_uz', models.CharField(max_length=100, null=True)),
                ('document_type_ru', models.CharField(max_length=100, null=True)),
                ('document_name', models.CharField(max_length=500)),
                ('document_name_en', models.CharField(max_length=500, null=True)),
                ('document_name_uz', models.CharField(max_length=500, null=True)),
                ('document_name_ru', models.CharField(max_length=500, null=True)),
                ('document', models.FileField(upload_to='pdf/')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name_en', models.CharField(max_length=100, null=True)),
                ('name_uz', models.CharField(max_length=100, null=True)),
                ('name_ru', models.CharField(max_length=100, null=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('body_en', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('body_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('body_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FinancialStatements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_type', models.CharField(max_length=100)),
                ('report_type_en', models.CharField(max_length=100, null=True)),
                ('report_type_uz', models.CharField(max_length=100, null=True)),
                ('report_type_ru', models.CharField(max_length=100, null=True)),
                ('quarter', models.CharField(max_length=100)),
                ('quarter_en', models.CharField(max_length=100, null=True)),
                ('quarter_uz', models.CharField(max_length=100, null=True)),
                ('quarter_ru', models.CharField(max_length=100, null=True)),
                ('pdf_file', models.FileField(upload_to='pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='Kafedra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name_en', models.CharField(max_length=100, null=True)),
                ('name_uz', models.CharField(max_length=100, null=True)),
                ('name_ru', models.CharField(max_length=100, null=True)),
                ('about', ckeditor_uploader.fields.RichTextUploadingField()),
                ('about_en', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('about_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('about_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UZFI.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='OpenData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', ckeditor.fields.RichTextField()),
                ('name_en', ckeditor.fields.RichTextField(null=True)),
                ('name_uz', ckeditor.fields.RichTextField(null=True)),
                ('name_ru', ckeditor.fields.RichTextField(null=True)),
                ('pdf_file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Requisites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unversit_name', models.CharField(max_length=100)),
                ('unversit_name_en', models.CharField(max_length=100, null=True)),
                ('unversit_name_uz', models.CharField(max_length=100, null=True)),
                ('unversit_name_ru', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100)),
                ('address_en', models.CharField(max_length=100, null=True)),
                ('address_uz', models.CharField(max_length=100, null=True)),
                ('address_ru', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('bank_account', models.CharField(max_length=100)),
                ('fax', models.CharField(max_length=100)),
                ('bank', models.CharField(max_length=100)),
                ('mfo', models.CharField(max_length=100)),
                ('INN', models.CharField(max_length=100)),
                ('OKONX', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', ckeditor.fields.RichTextField()),
                ('name_en', ckeditor.fields.RichTextField(null=True)),
                ('name_uz', ckeditor.fields.RichTextField(null=True)),
                ('name_ru', ckeditor.fields.RichTextField(null=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('body_en', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('body_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('body_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('views', models.IntegerField(default=0)),
                ('salary', models.CharField(max_length=100)),
                ('department', ckeditor.fields.RichTextField()),
                ('department_en', ckeditor.fields.RichTextField(null=True)),
                ('department_uz', ckeditor.fields.RichTextField(null=True)),
                ('department_ru', ckeditor.fields.RichTextField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('DEKAN', 'DEKAN'), ('MANAGER', 'MANAGER'), ('STUDENT', 'STUDENT')], max_length=50)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='KafedraTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('address_en', models.CharField(max_length=100, null=True)),
                ('address_uz', models.CharField(max_length=100, null=True)),
                ('address_ru', models.CharField(max_length=100, null=True)),
                ('img', models.ImageField(upload_to='img/')),
                ('biography', ckeditor_uploader.fields.RichTextUploadingField()),
                ('biography_en', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('biography_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('biography_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('kafedra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UZFI.kafedra')),
            ],
        ),
        migrations.CreateModel(
            name='KafedraManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('acceptance', models.CharField(max_length=200)),
                ('acceptance_en', models.CharField(max_length=200, null=True)),
                ('acceptance_uz', models.CharField(max_length=200, null=True)),
                ('acceptance_ru', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=100)),
                ('address_en', models.CharField(max_length=100, null=True)),
                ('address_uz', models.CharField(max_length=100, null=True)),
                ('address_ru', models.CharField(max_length=100, null=True)),
                ('img', models.ImageField(upload_to='img/')),
                ('duties', ckeditor_uploader.fields.RichTextUploadingField()),
                ('duties_en', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('duties_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('duties_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('kafedra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UZFI.kafedra')),
            ],
        ),
        migrations.CreateModel(
            name='DekanProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dekan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('acceptance', models.CharField(max_length=200)),
                ('acceptance_en', models.CharField(max_length=200, null=True)),
                ('acceptance_uz', models.CharField(max_length=200, null=True)),
                ('acceptance_ru', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=100)),
                ('address_en', models.CharField(max_length=100, null=True)),
                ('address_uz', models.CharField(max_length=100, null=True)),
                ('address_ru', models.CharField(max_length=100, null=True)),
                ('img', models.ImageField(upload_to='img/')),
                ('duties', ckeditor_uploader.fields.RichTextUploadingField()),
                ('duties_en', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('duties_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('duties_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('dekan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UZFI.dekanprofile')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UZFI.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='CentersDepartmentsManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='img/')),
                ('Tasks', ckeditor_uploader.fields.RichTextUploadingField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('centers_departments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UZFI.centersdepartments')),
            ],
        ),
    ]
