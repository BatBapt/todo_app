from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)

    color = models.CharField(max_length=7, default="#FFFFFF")

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Task(models.Model):

    title = models.CharField(max_length=250)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')

    content = models.TextField(blank=True)

    created = models.DateField(blank=True, default=timezone.now)
    due_date = models.DateField(blank=True, default=timezone.now)

    done = models.BooleanField(default=False)

    date_done = models.DateField(blank=True, default=timezone.now)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
