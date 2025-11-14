from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(
        upload_to='profile_pics',
        default='profile_pics/default-profile.jpg',
        blank=True,
        null=True,
        verbose_name='Profile Picture'
    )

    class Meta:
        db_table = 'user'