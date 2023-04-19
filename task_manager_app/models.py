from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Board(models.Model):
    title = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Task(models.Model):

    STATUS_CHOICES = [
        ('todo','To Do'),
        ('inprogress','In Progress'),
        ('done','Done')
    ]

    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    board = models.ForeignKey(Board, on_delete=models.CASCADE)



    def __str__(self):
        return self.title