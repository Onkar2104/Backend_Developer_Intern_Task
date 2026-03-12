from django.db import models
from user.models import User
from project.models import Project

# Create your models here.


class daily_report(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    work_description = models.TextField()
    weather = models.CharField(max_length=50)
    worker_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now=models.CASCADE)