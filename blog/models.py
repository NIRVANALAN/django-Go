from django.db import models


# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ('-timestamp',)


class DiaryPost(models.Model):
    title = models.CharField(max_length=30)
    participants = models.CharField(max_length=50)
    body = models.TextField()
    timestamp = models.DateTimeField()
