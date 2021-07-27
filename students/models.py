from django.db import models

from users.models import CustomUser


class Student(models.Model):
    student = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, primary_key=True)
    started_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student.__str__()

    def username(self):
        return self.student.username

    def gender(self):
        return self.student.sex

    def phone_number(self):
        return self.student.phone_number
