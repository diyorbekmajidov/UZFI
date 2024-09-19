from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from .user import User
from .models import Faculty, Kafedra
from django.core.exceptions import ValidationError

def validate_file_size(value):
    filesize = value.size

    if filesize > 1000 * 2024:
        raise ValidationError("The maximum file size that can be uploaded is 2mb")
    else:
        return value

class Leadership(models.Model):
    number =    models.IntegerField(blank=True, null=True)
    rector       = models.OneToOneField(User, on_delete=models.CASCADE , related_name="rector")
    prorektor    = models.CharField(max_length=200, blank=True, null=True)
    first_name   = models.CharField(max_length=200, blank=True, null=True)
    email        = models.CharField(max_length=100, blank=True, null=True)
    phone        = models.CharField(max_length=100, blank=True, null=True)
    address      = models.CharField(max_length=100, blank=True, null=True)
    acceptance   = models.CharField(max_length=200, blank=True, null=True)
    img          = models.ImageField(upload_to='img/',blank=True, null=True, validators=[validate_file_size])
    duties       = RichTextUploadingField(blank=True, null=True)
    biography    = RichTextUploadingField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update  = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.first_name
    

class Dekan(models.Model):
    dekan        = models.OneToOneField(User, on_delete=models.CASCADE, related_name='dekan')
    faculty      = models.OneToOneField(Faculty, on_delete=models.CASCADE, related_name='faculty')
    name         = models.CharField(max_length=100, blank=True, null=True)
    email        = models.CharField(max_length=100, blank=True, null=True)
    phone        = models.CharField(max_length=100, blank=True, null=True)
    acceptance   = models.CharField(max_length=200, blank=True, null=True)
    address      = models.CharField(max_length=100, blank=True, null=True)
    img          = models.ImageField(upload_to='img/',blank=True, null=True,validators=[validate_file_size])
    duties       = RichTextUploadingField(blank=True, null=True)
    biography    = RichTextUploadingField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class KafedraManager(models.Model):
    kafedramanager = models.OneToOneField(User, on_delete=models.CASCADE, related_name='kafedramanager')
    kafedra        = models.OneToOneField(Kafedra, on_delete=models.CASCADE, related_name='kafedra')
    name           = models.CharField(max_length=100, blank=True, null=True)
    email          = models.CharField(max_length=100, blank=True, null=True)
    phone          = models.CharField(max_length=100, blank=True, null=True)
    acceptance     = models.CharField(max_length=200, blank=True, null=True)
    address        = models.CharField(max_length=100, blank=True, null=True)
    img            = models.ImageField(upload_to='img/', blank=True, null=True, validators=[validate_file_size])
    duties         = RichTextUploadingField(blank=True, null=True)
    biography      = RichTextUploadingField(blank=True, null=True)
    date_created   = models.DateTimeField(auto_now_add=True)
    date_update    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 
    

class Tutor(models.Model):
    faculty        = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    general_information = RichTextUploadingField(blank=True, null=True)
    Task_tutors    = RichTextUploadingField(blank=True, null=True)
    full_name      = models.CharField(max_length=100)
    tutor_groups   = models.CharField(max_length=100000)
    phone          = models.CharField(max_length=100, blank=True, null=True)
    address        = models.CharField(max_length=100, blank=True, null=True)
    img            = models.ImageField(upload_to='img/', blank=True, null=True, validators=[validate_file_size])
    date_created   = models.DateTimeField(auto_now_add=True)
    date_update    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name 