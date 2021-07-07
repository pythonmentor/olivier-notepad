from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    date_of_birth = models.DateField("date_of_birth")

    class Meta:
        ordering = ['last_name']
    
    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name} {self.date_of_birth}"