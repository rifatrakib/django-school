from django.db import models

from users.models import CustomUser


class Student(models.Model):
    student = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, primary_key=True)
    identity = models.CharField(unique=True, max_length=50)
    started_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student.__str__()} - {self.identity}'
