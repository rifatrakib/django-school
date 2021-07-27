from django.db import models

from users.models import CustomUser


class Teacher(models.Model):
    teacher = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, primary_key=True)
    started_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.teacher.__str__()

    def username(self):
        return self.teacher.username

    def gender(self):
        return self.teacher.sex

    def phone_number(self):
        return self.teacher.phone_number
