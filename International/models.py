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
    title         = models.CharField(max_length=255)
    img           = models.ImageField(upload_to='img/', validators=[validate_file_size])
    body          = RichTextUploadingField()
    date_created  = date_created  = models.DateField()
    date_update   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    
class InternationalMemorandum(models.Model):
    title = models.CharField(max_length=100)
    body = RichTextUploadingField()
    img     = models.ImageField(upload_to='img/', validators=[validate_file_size])
    date_created  = models.DateField(auto_now=True)
    date_update   = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

class InternationalGrant(models.Model):
    title = models.CharField(max_length=100)
    body = RichTextUploadingField()

    def __str__(self) -> str:
        return self.title

class InternationalGrantImg(models.Model):
    img     = models.ImageField(upload_to='img/', validators=[validate_file_size])
    grant   = models.ForeignKey(InternationalGrant, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.grant.id)
    

class Abitur(models.Model):
    title = models.CharField(max_length=150)
    body  = RichTextUploadingField()

    def _str__(self)-> str:
        return str(self.title)
    
class StudentGroups(models.Model):
    title = models.CharField(max_length=100)
    body = RichTextUploadingField()

    def __str__(self) -> str:
        return self.title 