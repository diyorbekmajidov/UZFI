from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        DEKAN     = "DEKAN", "DEKAN"
        REKTOR    = "REKTOR", "REKTOR"
        PROREKTOR = "PROREKTOR", "PROREKTOR"
        MANAGER   = "KAFEDRAMANAGER", "KAFEDRAMANAGER"
        ADMIN     = "ADMIN", "ADMIN"

    role = models.CharField(max_length=50, choices=Role.choices)

    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         self.role = self.role.upper()
    #         return super().save(*args, **kwargs)




