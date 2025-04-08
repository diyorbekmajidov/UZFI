from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.exceptions import ValidationError


class NewsCategory(models.Model):
    new_category = models.CharField(max_length=255,)

    def __str__(self) -> str:
        return self.new_category
    
    class Meta:
        verbose_name = "Yangiliklar_toifasi"
    
    
def validate_file_size(value):
    filesize = value.size

    if filesize > 1000 * 2024:
        raise ValidationError("The maximum file size that can be uploaded is 2mb")
    else:
        return value
    
class News_Content(models.Model):
    category      = models.ManyToManyField(NewsCategory, verbose_name='kategoriya')
    title         = models.CharField(max_length=255, verbose_name='sarlavha')
    img           = models.ImageField(upload_to='img/', validators=[validate_file_size], verbose_name='rasm')
    body          = RichTextUploadingField(verbose_name='matn tanasi')
    views         = models.IntegerField(default=0, verbose_name="ko'rishlar soni")
    date_created  = models.DateField()
    date_update   = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Yangiliklar"

    def __str__(self):
        return self.title or ""
    

class Vedio_New(models.Model):
    title         = models.CharField(max_length=255, verbose_name='sarlavha')
    vedio         = models.CharField(max_length = 10055)
    body          = models.ImageField(upload_to='img/', verbose_name='matn tanasi') 
    views         = models.IntegerField(default=0, verbose_name="ko'rishlar soni")
    date_created  = models.DateField(auto_now_add=True)
    date_update   = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Video Yangiliklar"
    
    def __str__(self):
        return self.title
    

class PopularStudents(models.Model):
    student_name  = models.CharField(max_length=150, verbose_name='talaba ismi')
    body          = RichTextUploadingField(verbose_name='matn tanasi')
    description   = models.CharField(max_length=300, verbose_name='tavsifi')
    date_created  = models.DateField(auto_now_add=True)
    date_update   = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Mashhur_talabalar"

    def __str__(self) -> str:
        return self.student_name
    
class PopularStudentImg(models.Model):
    popular = models.ForeignKey(PopularStudents,on_delete=models.CASCADE, verbose_name='mashhur')
    img     = models.ImageField(upload_to='img/', validators=[validate_file_size], verbose_name='rasm')

    def __str__(self) -> str:
        return self.popular.student_name
    class Meta:
        verbose_name = "Mashhur_talabalar_rasm"

class UploadFile(models.Model):
    file = models.FileField(upload_to='files/')
    title = models.CharField(max_length=255, verbose_name='sarlavha')
    date_created  = models.DateField(auto_now_add=True)
    date_update   = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.file.name
    def get_file_link(self):
        return 'https://uzfi.uz/'+self.file.url
    
    class Meta:
        verbose_name = "Faylni_yuklash"

    
class PendingEvents(models.Model):
    event_name    = models.CharField(max_length=150, verbose_name='tadbir nomi')
    place         = models.CharField(max_length=150, verbose_name='manzil')
    start_date    = models.DateField(verbose_name='boshlanish sanasi')
    views         = models.IntegerField(default=0, verbose_name="ko'rishlar soni")
    body          = RichTextUploadingField(verbose_name='matn tanasi')
    img     = models.ImageField(upload_to='img/', validators=[validate_file_size], verbose_name='rasm')
    date_created  = models.DateField()
    date_update   = models.DateTimeField(auto_now=True)

    def __str__(self) ->str:
        return self.event_name
    class Meta:
        verbose_name = "E'lonlar"
    
    