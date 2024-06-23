from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile, UserProfile


@receiver(post_save, sender=Profile)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(profile=instance)
