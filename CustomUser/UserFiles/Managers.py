from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as ul

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError(ul('The Email Must be Set '))
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        
        return user
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_admin',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        if extra_fields.get('is_admin') is not True:
            raise ValueError(ul('SUper user Must Be have the is_admin=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(ul('Super user must have the is_superuser=True'))
        return self.create_user(email,password,**extra_fields)
        