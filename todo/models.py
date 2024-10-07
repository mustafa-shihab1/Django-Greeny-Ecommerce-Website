from django.db import models


class ToDo(models.Model):
    title = models.CharField(max_length=100)
    done = models.BooleanField(default=False)