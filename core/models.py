from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("E-mail", unique=True)

    first_name = models.CharField("First name", max_length=30, blank=True)
    last_name = models.CharField("Last name", max_length=30, blank=True)

    date_joined = models.DateTimeField("date joined", auto_now_add=True)

    is_active = models.BooleanField("User active?", default=True)
    is_staff = models.BooleanField("Staff?", default=False)
    is_superuser = models.BooleanField("Superuser?", default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"

    class Meta:
        ordering = ["first_name", "last_name"]
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "users"

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name or "Unamed"
