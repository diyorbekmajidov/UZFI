from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.exceptions import ValidationError

def validate_file_size(value):
    filesize = value.size

    if filesize > 1000 * 2024:
        raise ValidationError("The maximum file size that can be uploaded is 2mb")
    else:
        return value
    

class InternationalRelation(models.Model):
    title         = models.CharField(max_length=255, verbose_name='sarlavha')
    img           = models.ImageField(upload_to='img/', validators=[validate_file_size], verbose_name='rasm')
    body          = RichTextUploadingField(verbose_name='matn_tanasi')
    date_created  = models.DateField()
    date_update   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Xalqaro_aloqalar"

    
class InternationalMemorandum(models.Model):
    title = models.CharField(max_length=100, verbose_name='sarlavha')
    body = RichTextUploadingField(verbose_name='matn_tanasi')
    img     = models.ImageField(upload_to='img/', validators=[validate_file_size], verbose_name='rasm')
    date_created  = models.DateField(auto_now=True)
    date_update   = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name="Xalqaro_memorandum"

class InternationalGrant(models.Model):
    title = models.CharField(max_length=100, verbose_name='sarlavha')
    body = RichTextUploadingField(verbose_name='matn_tanasi')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Xalqaro_grant"

class InternationalGrantImg(models.Model):
    img     = models.ImageField(upload_to='img/', validators=[validate_file_size])
    grant   = models.ForeignKey(InternationalGrant, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.grant.id)
    
    class Meta:
        verbose_name = "Xalqaro_grant_rasm"
    

class Abitur(models.Model):
    title = models.CharField(max_length=150, verbose_name="sarlavha")
    body  = RichTextUploadingField(verbose_name="matn_tanasi")

    def _str__(self)-> str:
        return str(self.title)
    
    class Meta:
        verbose_name="Abiturint"
    
class StudentGroups(models.Model):
    title = models.CharField(max_length=100, verbose_name="sarlavha")
    body = RichTextUploadingField(verbose_name="matn_tanasi")

    def __str__(self) -> str:
        return self.title 
    
    class Meta:
        verbose_name="Talabalar_guruhlari"