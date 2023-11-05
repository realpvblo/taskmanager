from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateField()
    priority = models.CharField(max_length=20)

    def __str__(self):
        return self.title