from django.db import models

# Create your models here.

class User(models.Model):

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('worker', 'Worker')
    )

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    password_hash = models.CharField(max_length=200)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.email
