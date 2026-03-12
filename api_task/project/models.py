from django.db import models
from user.models import User

# Create your models here.

class Project(models.Model):

    STATUS_CHOICES = (
        ('planned', 'Planned'),
        ('active', 'Active'),
        ('completed', 'Completed')
    )

    name = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=10)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)