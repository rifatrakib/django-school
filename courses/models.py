from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    credit = models.PositiveIntegerField()

    def __str__(self):
        return self.title
