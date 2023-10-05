from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    def save(self, *args, **kwargs):

        self.is_active = True

        super(User, self).save(*args, **kwargs)

        