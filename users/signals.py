from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import CustomUser, Profile
from courses.models import Enrollment


@receiver(post_save, sender=CustomUser)
def post_save_create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)
