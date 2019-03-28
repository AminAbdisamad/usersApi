from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class UserProfileManager(AbstractBaseUser):
    def create_user(self, name, email, password=None):
        if not email:
            raise ValueError("User must have email ")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, password):
        user = self.create_user(name, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ creating a custom Model for user Profiles"""

    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELD = ["name"]

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        """ converts object to string  """
        return self.email

