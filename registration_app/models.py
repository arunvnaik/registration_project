from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('private', 'Private'),
        ('public', 'Public'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='private')
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='registration_app_users',  # Add related_name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='registration_app_users',  # Add related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Image(models.Model):
    user = models.ForeignKey(User, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/')
    timestamp = models.DateTimeField(auto_now_add=True)
