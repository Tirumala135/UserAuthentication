from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as ul

from .UserFiles.Managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(ul('Email Address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    number = PhoneNumberField(ul("Mobile Number"), max_length=20)
    date_of_birth = models.DateField()

    # Set unique related names for groups and user_permissions
    groups = models.ManyToManyField(Group, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users')

    # class Meta:
    #     ordering = ['id']  # Adjust the ordering field as needed

    def __str__(self):
        return f"\t {self.email} \t {self.number}"
