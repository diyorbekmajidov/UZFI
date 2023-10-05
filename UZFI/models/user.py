from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'admin'
        DEKAN   = "DEKAN", "DEKAN"
        MANAGER = "KAFEDRAMANAGER", "KAFEDRAMANAGER"
        TEACHER = "TEACHER", "TEACHER"

    role = models.CharField(max_length=50, choices=Role.choices)

    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         self.role = self.role.upper()
    #         return super().save(*args, **kwargs)




