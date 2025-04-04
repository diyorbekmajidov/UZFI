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
    number =    models.IntegerField(blank=True, null=True, verbose_name="id")
    rector       = models.OneToOneField(User, on_delete=models.CASCADE , related_name="rector", verbose_name="rektor")
    prorektor    = models.CharField(max_length=200, blank=True, null=True, verbose_name="prorektor")
    first_name   = models.CharField(max_length=200, blank=True, null=True, verbose_name="ismi")
    email        = models.CharField(max_length=100, blank=True, null=True)
    phone        = models.CharField(max_length=100, blank=True, null=True, verbose_name="telfon_raqam")
    address      = models.CharField(max_length=100, blank=True, null=True, verbose_name="manzil")
    acceptance   = models.CharField(max_length=200, blank=True, null=True, verbose_name="qabul_kunlari")
    img          = models.ImageField(upload_to='img/',blank=True, null=True, validators=[validate_file_size], verbose_name="rasm")
    duties       = RichTextUploadingField(blank=True, null=True, verbose_name="vazifalar")
    biography    = RichTextUploadingField(blank=True, null=True, verbose_name="biografiyasi")
    date_created = models.DateTimeField(auto_now_add=True)
    date_update  = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.first_name or ""
    
    class Meta:
        verbose_name = "Rahbariyat"
    

class Dekan(models.Model):
    dekan        = models.OneToOneField(User, on_delete=models.CASCADE, related_name='dekan')
    faculty      = models.OneToOneField(Faculty, on_delete=models.CASCADE, related_name='faculty')
    name         = models.CharField(max_length=100, blank=True, null=True, verbose_name="nomi")
    email        = models.CharField(max_length=100, blank=True, null=True)
    phone        = models.CharField(max_length=100, blank=True, null=True, verbose_name="telfon_raqam")
    acceptance   = models.CharField(max_length=200, blank=True, null=True, verbose_name='qabul_kunlari')
    address      = models.CharField(max_length=100, blank=True, null=True, verbose_name="manzil")
    img          = models.ImageField(upload_to='img/',blank=True, null=True,validators=[validate_file_size], verbose_name='rasm')
    duties       = RichTextUploadingField(blank=True, null=True, verbose_name="vazifalar")
    biography    = RichTextUploadingField(blank=True, null=True, verbose_name="biografiyasi")
    date_created = models.DateTimeField(auto_now_add=True)
    date_update  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.faculty.name
    
    class Meta:
        verbose_name = "Dekan"
    

class KafedraManager(models.Model):
    kafedramanager = models.OneToOneField(User, on_delete=models.CASCADE, related_name='kafedramanager', verbose_name="kafedra_mudur")
    kafedra        = models.OneToOneField(Kafedra, on_delete=models.CASCADE, related_name='kafedra', verbose_name="kafedra")
    name           = models.CharField(max_length=100, blank=True, null=True, verbose_name="nomi")
    email          = models.CharField(max_length=100, blank=True, null=True)
    phone          = models.CharField(max_length=100, blank=True, null=True,verbose_name="telfon_raqam")
    acceptance     = models.CharField(max_length=200, blank=True, null=True, verbose_name='qabul_kunlari')
    address        = models.CharField(max_length=100, blank=True, null=True, verbose_name="manzil")
    img            = models.ImageField(upload_to='img/', blank=True, null=True, validators=[validate_file_size], verbose_name="rasm")
    duties         = RichTextUploadingField(blank=True, null=True, verbose_name="vazifalar")
    biography      = RichTextUploadingField(blank=True, null=True, verbose_name="biografiyasi")
    date_created   = models.DateTimeField(auto_now_add=True)
    date_update    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.kafedra.name 
    
    class Meta:
        verbose_name = "Kafedra_menejeri"
    

class Tutor(models.Model):
    faculty        = models.ForeignKey(Faculty, on_delete=models.CASCADE, verbose_name="fakultet")
    general_information = RichTextUploadingField(blank=True, null=True, verbose_name="Umumiy_ma'lumot")
    Task_tutors    = RichTextUploadingField(blank=True, null=True, verbose_name="vaifalar")
    full_name      = models.CharField(max_length=100, verbose_name="to'liq_ism")
    tutor_groups   = models.CharField(max_length=100000)
    phone          = models.CharField(max_length=100, blank=True, null=True, verbose_name="telfon_raqam")
    address        = models.CharField(max_length=100, blank=True, null=True, verbose_name="manzil")
    img            = models.ImageField(upload_to='img/', blank=True, null=True, validators=[validate_file_size], verbose_name="rasm")
    date_created   = models.DateTimeField(auto_now_add=True)
    date_update    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.phone