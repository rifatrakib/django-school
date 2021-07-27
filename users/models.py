from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


ROLES = (
    ('Student', 'Student'),
    ('Teacher', 'Teacher'),
)

GENDERS = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)


class CustomUser(AbstractUser):
    sex = models.CharField(choices=GENDERS, max_length=10)
    role = models.CharField(choices=ROLES, max_length=20)
    birthday = models.DateTimeField(blank=True, null=True)
    phone_number = PhoneNumberField(unique=True, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars', default='blank.png')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Profile(models.Model):
    owner = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(blank=True, null=True, max_length=250)
    cover = models.ImageField(upload_to='covers', default='default_cover.png')

    def __str__(self):
        return self.owner.__str__()
