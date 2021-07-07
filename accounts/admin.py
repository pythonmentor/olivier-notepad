
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from django.utils.translation import gettext, gettext_lazy as _

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = (
    'email',
    'username',
    'first_name', 
    'last_name',
    'date_of_birth',
    )      

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth', 'username', 'first_name', 'last_name')}),
    )