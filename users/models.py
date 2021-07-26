from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


ROLES = (
    ('Admin', 'Admin'),
    ('Student', 'Student'),
    ('Teacher', 'Teacher'),
    ('Parents', 'Parents'),
    ('Supervisor', 'Supervisor'),
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
