from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True, db_index=True)
    email = models.EmailField(_('email address'), max_length=50, unique=True)
    is_email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username
