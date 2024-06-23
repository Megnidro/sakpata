from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self.create_user(email, password, **extra_fields)


class Profile(AbstractUser):
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'last_name', 'first_name']
    objects = CustomUserManager()

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('passager', 'passager'),
        ('driver', 'conducteur'),
        ('alternant', 'alternant'),
    ]

    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='user_profile', unique=True)

    # Informations personnelles complémentaires
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    # Rôle de l'utilisateur
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='passager')

    # Préférences de covoiturage
    smoker = models.BooleanField(default=False)
    pets_allowed = models.BooleanField(default=False)
    music_preferences = models.CharField(max_length=100, blank=True, null=True)
    chat_preferences = models.CharField(max_length=100, blank=True, null=True)

    # Statistiques
    total_trips_offered = models.IntegerField(default=0)
    total_trips_taken = models.IntegerField(default=0)

    # Préférences de notification
    email_notifications = models.BooleanField(default=True)
    sms_notifications = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.profile.email}'s profile"
