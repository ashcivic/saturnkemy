from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class TaskList(models.Model):
    name = models.CharField(max_length=200, editable=True)

    def __str__(self):
        return "Name: {} | Cards: {}".format(self.name, self.card_set.all())


class Card(models.Model):
    task_list = models.ForeignKey('TaskList', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, editable=True)
    description = models.TextField(default='')
    timestamp = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(blank=True, null=True)

    activity_log = models.TextField(default="Card created | {}".format(
                                                            timezone.now()))

    def __str__(self):
        if self.due_date is None:
            return "Name: {} | Description: {}".format(self.name,
                                                       self.description)
        else:
            return "Name: {} | Description: {} | Due Date: {}".format(
                                                            self.name,
                                                            self.description,
                                                            self.due_date)
