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
    



class Faculty(models.Model):
    name = models.CharField(max_length=100)
    body = RichTextUploadingField()

    def __str__(self):
        return self.name
    
class Dekan(models.Model):
    dekan        = models.OneToOneField(User, on_delete=models.CASCADE)
    faculty      = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    name         = models.CharField(max_length=100)
    email        = models.CharField(max_length=100)
    phone        = models.CharField(max_length=100)
    acceptance   = models.CharField(max_length=200)
    address      = models.CharField(max_length=100)
    img          = models.ImageField(upload_to='img/')
    duties       = RichTextUploadingField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_update  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Kafedra(models.Model):
    faculty      = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    name         = models.CharField(max_length=100)
    about        = RichTextUploadingField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_update  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class KafedraManager(models.Model):
    kafedra      = models.ForeignKey(Kafedra, on_delete=models.CASCADE)
    name         = models.CharField(max_length=100)
    email        = models.CharField(max_length=100)
    phone        = models.CharField(max_length=100)
    acceptance   = models.CharField(max_length=200)
    address      = models.CharField(max_length=100)
    img          = models.ImageField(upload_to='img/')
    duties       = RichTextUploadingField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_update  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class KafedraTeacher(models.Model):
    kafedra         = models.ForeignKey(Kafedra, on_delete=models.CASCADE)
    name            = models.CharField(max_length=100)
    email           = models.CharField(max_length=100)
    phone           = models.CharField(max_length=100)
    address         = models.CharField(max_length=100)
    img             = models.ImageField(upload_to='img/')
    biography       = RichTextUploadingField()
    date_created    = models.DateTimeField(auto_now_add=True)
    date_update     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class CentersDepartments(models.Model):
    name = models.CharField(max_length=100)
    body = RichTextUploadingField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_update  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class CentersDepartmentsManager(models.Model):
    centers_departments = models.ForeignKey(CentersDepartments, on_delete=models.CASCADE)
    name                = models.CharField(max_length=100)
    email               = models.CharField(max_length=100)
    phone               = models.CharField(max_length=100)
    address             = models.CharField(max_length=100)
    img                 = models.ImageField(upload_to='img/')
    Tasks               = RichTextUploadingField()
    date_created        = models.DateTimeField(auto_now_add=True)
    date_update         = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
