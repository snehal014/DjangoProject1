from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    address = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "tblclient"

    def __str__(self):
        return self.name

class Project(models.Model):
    client = models.ForeignKey(Client, related_name='projects', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    users = models.ManyToManyField(User, through='ProjectAssignment', related_name='assigned_projects')  # Many-to-many relationship with User

    class Meta:
        db_table = "tblproject"

    def __str__(self):
        return self.name

class ProjectAssignment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "tblprojectassignment"
        unique_together = ('project', 'user')
