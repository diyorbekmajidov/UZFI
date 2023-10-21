from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from .user import User



class Charter(models.Model):
    title        = RichTextField()
    body         = RichTextUploadingField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_update  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Document(models.Model):
    document_type = models.CharField(max_length=100)
    document_name = models.CharField(max_length=500)
    document      = models.FileField(upload_to='pdf/')
    date_created  = models.DateTimeField(auto_now_add=True)
    date_update   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.document_type
    
class Councils(models.Model):
    id           = models.AutoField(primary_key=True)
    title        = RichTextField()
    body         = RichTextUploadingField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_update  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Requisites(models.Model):
    unversit_name = models.CharField(max_length=100)
    address       = models.CharField(max_length=100)
    phone         = models.CharField(max_length=100)
    email         = models.CharField(max_length=100)
    bank_account  = models.CharField(max_length=100)
    fax           = models.CharField(max_length=100)
    bank          = models.CharField(max_length=100)
    mfo           = models.CharField(max_length=100)
    INN           = models.CharField(max_length=100)
    OKONX         = models.CharField(max_length=100)
    date_created  = models.DateTimeField(auto_now_add=True)
    date_update   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.unversit_name
    
class FinancialStatements(models.Model):
    report_type = models.CharField(max_length=100)
    quarter     = models.CharField(max_length=100)
    pdf_file    = models.FileField(upload_to='pdf/')
    # date_created  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.report_type
    
class OpenData(models.Model):
    name       = RichTextField()
    pdf_file   = models.FileField()

    def __str__(self):
        return self.name
    
class Vacancies(models.Model):
    name         = RichTextField()
    body         = RichTextUploadingField()
    views        = models.IntegerField(default=0)
    salary       = models.CharField(max_length=100)
    department   = RichTextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_update  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class ScientificWork(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE, related_name="scientific")
    article_name     = models.CharField(max_length=100, blank=True, null=True)
    article_level    = models.CharField(max_length=100, blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)
    link             = models.CharField(max_length=100, blank=True, null=True)
    pdf_file         = models.FileField(upload_to='pdf/', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update  = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.article_name

class Faculty(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Kafedra(models.Model):
    faculty      = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    name         = models.CharField(max_length=100)
    about        = RichTextUploadingField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Direction(models.Model):
    faculty    = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    name       = models.CharField(max_length=150)
    about      = RichTextUploadingField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

class CentersDepartments(models.Model):
    name = models.CharField(max_length=100)
    body = RichTextUploadingField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_update  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class CentersDepartmentsManager(models.Model):
    centers_departments = models.OneToOneField(CentersDepartments, on_delete=models.CASCADE)
    name                = models.CharField(max_length=100)
    email               = models.CharField(max_length=100)
    phone               = models.CharField(max_length=100)
    address             = models.CharField(max_length=100)
    img                 = models.ImageField(upload_to='img/')
    tasks               = RichTextUploadingField()
    date_created        = models.DateTimeField(auto_now_add=True)
    date_update         = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
