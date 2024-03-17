from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email or not password:
            raise ValueError('Wpisz email i hasło')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_superuser(email, password=password, **extra_fields)
    
    def authenticate(self, request, email, password, **extra_fields):
        try:
            user = self.get(email=email)
        except self.model.DoesNotExist:
            return None
        
        if user.check_password(password):
            return user
        
        return None
    
def user_profile_picture_path(instance, filename):
    return f'user_profiles/{instance.id}/{filename}'


class CustomUser(AbstractUser):
    objects = CustomUserManager()
    username = models.CharField(max_length=32, unique=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    date_of_birth = models.DateField()
    email = models.EmailField(max_length=64)
    profile_picture = models.ImageField(upload_to=user_profile_picture_path, null=True, blank=True)
    description = models.TextField(max_length=200, null=True)
    
    