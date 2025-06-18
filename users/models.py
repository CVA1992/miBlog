from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Campos adicionales al User predeterminado
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(
        upload_to='profile_pics/',
        blank=True,
        null=True
    )
    website = models.URLField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.username