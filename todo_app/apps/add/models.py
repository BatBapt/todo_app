from django.db import models
from django.utils import timezone


class Task(models.Model):

    name = models.CharField(max_length=250)

    content = models.TextField(blank=True)

    created = models.DateField(default=timezone.now().strftime("%d-%m-%Y"))
    due_date = models.DateField(default=timezone.now().strftime("%d-%m-%Y"))

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name
