from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('email is required')
        user = self.model(
            email = self.normalize_email(email), 
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password = None):
        user = self.create_user(
            email = self.normalize_email(email),
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", unique=True)
    Date_joined = models.DateTimeField(verbose_name = "date_joined", auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = MyUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
