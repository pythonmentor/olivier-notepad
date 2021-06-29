from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from django.core.validators import RegexValidator


class CustomUser(AbstractUser):
    date_of_birth = models.DateField("date_of_birth", blank=True, null=True)

    class Meta:
        ordering = ['last_name']
    
    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name} {self.date_of_birth}"