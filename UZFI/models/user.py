from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'admin'
        DEKAN   = "DEKAN", "DEKAN"
        MANAGER = "MANAGER", "MANAGER"
        TEACHER = "TEACHER", "TEACHER"

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.role.upper()
            return super().save(*args, **kwargs)

# class DekanManager(BaseUserManager):
#     def get_queryset(self, *args, **kwargs):
#         results = super().get_queryset(*args, **kwargs)
#         return results.filter(role=User.Role.DEKAN)

# class ManagerManager(BaseUserManager):
#     def get_queryset(self, *args, **kwargs):
#         results = super().get_queryset(*args, **kwargs)
#         return results.filter(role=User.Role.MANAGER)


# class DekanProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     student_id = models.IntegerField(null=True, blank=True)

# class ManagerProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     student_id = models.IntegerField(null=True, blank=True)
