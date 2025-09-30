
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class User(AbstractUser):
    ROLE_SUPERADMIN = 'superadmin'
    ROLE_ADMIN = 'admin'
    ROLE_USER = 'user'
    ROLE_CHOICES = [
        (ROLE_SUPERADMIN, 'SuperAdmin'),
        (ROLE_ADMIN, 'Admin'),
        (ROLE_USER, 'User'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ROLE_USER)

    # optional: assign each user to an admin
    assigned_admin = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='assigned_users',
        limit_choices_to={'role': ROLE_ADMIN},
    )

    def is_superadmin(self):
        return self.role == self.ROLE_SUPERADMIN

    def is_admin(self):
        return self.role == self.ROLE_ADMIN
