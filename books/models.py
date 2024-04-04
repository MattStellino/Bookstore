from django.db import models
from django.conf import settings

class BookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('title')

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    rating = models.FloatField()
    description = models.TextField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='books'
    )

    objects = BookManager()

    def __str__(self):
        return self.title
