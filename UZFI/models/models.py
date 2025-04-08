from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from .user import User
from django.core.exceptions import ValidationError
  

def validate_file_size(value):
    filesize = value.size
    if filesize > 1000 * 1024:
        raise ValidationError("The maximum file size that can be uploaded is 1mb")
    else:
        return value
    
class Menu(models.Model):
    title = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update  = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class SubMenu(models.Model):
    title = models.CharField(max_length=50, verbose_name='Nomi')
    sub_menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    number = models.IntegerField(blank=True, null=True, verbose_name="id")
    url = models.CharField(max_length=50,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class GreenInstitute(models.Model):
    title = models.CharField(max_length=50, verbose_name='Nomi')
    body = RichTextUploadingField(blank=True, null=True, verbose_name='matn tanasi')
    date_created = models.DateTimeField(auto_now_add=True)
    date_update  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Yashil institut"
        verbose_name_plural = "Yashil institut"

class Charter(models.Model):
    title        = models.CharField(max_length=255, verbose_name="sarlavha")
    body         = RichTextUploadingField(verbose_name="matn tanasi")
    date_created = models.DateTimeField(auto_now_add=True)
    date_update  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Nizom"
        verbose_name_plural = "Nizom"
    
class Document(models.Model):
    document_type = models.CharField(max_length=100, verbose_name='hujjat turi')
    document_name = models.CharField(max_length=500, verbose_name="hujjat nomi")
    document      = models.FileField(upload_to='pdf/', verbose_name="hujjat")
    date_created  = models.DateField(auto_now_add=True)
    date_update   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.document_type
    
    class Meta:
        verbose_name = "Hujjatlar"
    
class Councils(models.Model):
    id           = models.AutoField(primary_key=True)
    title        = models.CharField(max_length=255, verbose_name="sarlavha")
    body         = RichTextUploadingField(verbose_name="matn tanasi")
    date_created = models.DateField(auto_now_add=True)
    date_update  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Kengashlar"

class Requisites(models.Model):
    unversit_name = models.CharField(max_length=100, verbose_name="institut nomi")
    address       = models.CharField(max_length=100, verbose_name="manzil")
    phone         = models.CharField(max_length=100, verbose_name="telfon raqam")
    email         = models.CharField(max_length=100)
    bank_account  = models.CharField(max_length=100, verbose_name='bank raqam')
    fax           = models.CharField(max_length=100)
    bank          = models.CharField(max_length=100)
    mfo           = models.CharField(max_length=100)
    INN           = models.CharField(max_length=100)
    OKONX         = models.CharField(max_length=100)
    date_created  = models.DateTimeField(auto_now_add=True)
    date_update   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.unversit_name
    
    class Meta:
        verbose_name = "Rekvizitlar"
    
    
    
class OpenData(models.Model):
    name       = models.CharField(max_length=255, verbose_name="nomi")
    pdf_file   = models.FileField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Ochiq_ma'lumotlar"
    

    

class Faculty(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name="nomi")
    body = RichTextUploadingField(blank=True, null=True, verbose_name='matn tanasi')
    img  = models.ImageField(upload_to='img/',validators=[validate_file_size])

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Fakultetlar"
    
class Kafedra(models.Model):
    img          = models.ImageField(upload_to='img/',blank=None, null=True,validators=[validate_file_size])
    faculty      = models.ForeignKey(Faculty, on_delete=models.CASCADE, verbose_name='fakultet')
    name         = models.CharField(max_length=100, verbose_name='nomi')
    about        = RichTextUploadingField(blank=True, null=True, verbose_name='fakultet haqida')
    date_created = models.DateTimeField(auto_now_add=True)
    date_update  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Kafedralar"
    
class Direction(models.Model):
    faculty    = models.ForeignKey(Faculty, on_delete=models.CASCADE, verbose_name="fakultet")
    img        = models.ImageField(upload_to='img/', blank=True, null=True,validators=[validate_file_size])
    name       = models.CharField(max_length=150, verbose_name='nomi')
    direction_type= models.CharField(default="bakalavir", max_length=20, verbose_name="yo'nalish_turi") # direction or specialization
    about      = RichTextUploadingField(blank=True, null=True, verbose_name="yo'nalish_haqida")
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Yo'nalishlar"

class CentersDepartments(models.Model):
    class Role(models.TextChoices):
        MARKAZ     = "MARKAZ", "MARKAZ"
        BULIM     = "BO'LIM", "BO'LIM"
    role = models.CharField(max_length=50, choices=Role.choices, blank=True, null=True, verbose_name="roli")
    name = models.CharField(max_length=100, verbose_name="nomi")
    number = models.IntegerField(blank=True, null=True, verbose_name="id")
    body = RichTextUploadingField(verbose_name="matn tanasi")
    date_created = models.DateTimeField(auto_now_add=True)
    date_update  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Markazlar_bo'limlari"
class CentersDepartmentsManager(models.Model):
    councils = models.OneToOneField(Councils, on_delete=models.CASCADE, blank=True, null=True, verbose_name="kengashlar")
    centers_departments = models.OneToOneField(CentersDepartments, on_delete=models.CASCADE, blank=True, null=True, verbose_name="markazlar")
    acceptance     = models.CharField(max_length=200, blank=True, null=True, verbose_name="qabul_kunlari")
    lavozim        = models.CharField(max_length=30, blank=True, null=True)
    name           = models.CharField(max_length=100, verbose_name="ismi")
    email          = models.CharField(max_length=100)
    phone          = models.CharField(max_length=100, verbose_name="telfon_raqam")
    address        = models.CharField(max_length=100, verbose_name="manzil")
    img            =models.ImageField(upload_to='img/', blank=True, null=True,validators=[validate_file_size])
    date_created   = models.DateTimeField(auto_now_add=True)
    date_update    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.email
    
    class Meta:
        verbose_name = "Markazlar_bo'limlari_boshlig'i"
    
