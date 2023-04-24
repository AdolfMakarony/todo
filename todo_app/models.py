from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# def add_data(apps, schema):
class TodoList(models.Model):
    # id = models.IntegerField(primary_key=True) samo soboi propisivaetsyz
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()

class TodoStatus(models.Model):
    name = models.TextField()

class TodoTask(models.Model):
    todo_list = models.ForeignKey(TodoList, models.CASCADE)
    create_at = models.DateTimeField()
    complete_at = models.DateTimeField(null=True)
    status = models.ForeignKey(TodoStatus, models.CASCADE)
    title = models.TextField()
    text = models.TextField()


