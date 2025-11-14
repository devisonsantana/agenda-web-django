from django.contrib.auth.models import AbstractUser
from django.db import models

def upload_to(instace, filename):
    return f'profile_pics/{instace.username}/{filename}'

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(
        upload_to=upload_to,
        default='profile_pics/default-profile.jpg',
        blank=True,
        null=True,
        verbose_name='Profile Picture'
    )

    class Meta:
        db_table = 'user'