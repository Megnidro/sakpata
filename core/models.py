from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from compte.models import UserProfile


class Car(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='cars')
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    color = models.CharField(max_length=30)
    license_plate = models.CharField(max_length=20)
    seats = models.IntegerField(default=4)

    def __str__(self):
        return f"{self.owner.user.email}'s {self.make} {self.model}"

"""
@receiver(post_save, sender=UserProfile)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if UserProfile.role == 'driver' or UserProfile.role == 'alternant':
            Profile.objects.create(user=instance)
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=UserProfile)
def save_user_profile(sender, instance, **kwargs):
    instance.user_profile.save()"""


class DriverRating(models.Model):
    driver = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='ratings_received')
    passenger = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='ratings_given')
    rating = models.FloatField(default=0.0)
    comment = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('driver', 'passenger')

    def __str__(self):
        return f"Rating for {self.driver.user.email} by {self.passenger.user.email}"



class Trajet(models.Model):
    conducteur = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='trajets_proposes')
    depart = models.CharField(max_length=100)
    arrivee = models.CharField(max_length=100)
    date_depart = models.DateTimeField()
    places_disponibles = models.IntegerField(default=1)
    prix = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    voiture = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Trajet de {self.depart} à {self.arrivee} le {self.date_depart}"


class Reservation(models.Model):
    trajet = models.ForeignKey(Trajet, on_delete=models.CASCADE, related_name='reservations')
    passager = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reservations')
    nombre_places = models.IntegerField(default=1)
    statut = models.CharField(max_length=20, choices=[
        ('EN_ATTENTE', 'En attente'),
        ('CONFIRMEE', 'Confirmée'),
        ('ANNULEE', 'Annulée')
    ], default='EN_ATTENTE')

    def __str__(self):
        return f"Réservation de {self.passager.user.email} pour le trajet {self.trajet}"


class Reclamation(models.Model):
    auteur = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reclamations')
    trajet = models.ForeignKey(Trajet, on_delete=models.CASCADE, related_name='reclamations')
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=[
        ('OUVERTE', 'Ouverte'),
        ('EN_COURS', 'En cours de traitement'),
        ('RESOLUE', 'Résolue'),
        ('FERMEE', 'Fermée')
    ], default='OUVERTE')

    def __str__(self):
        return f"Réclamation de {self.auteur.user.email} pour le trajet {self.trajet}"


class Notification(models.Model):
    destinataire = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='notifications')
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    lue = models.BooleanField(default=False)

    # Pour lier la notification à différents types d'objets (trajet, réclamation, etc.)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    contenu_objet = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"Notification pour {self.destinataire.user.email}: {self.contenu[:50]}..."


class Recompense(models.Model):
    conducteur = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='recompenses')
    description = models.CharField(max_length=200)
    points = models.IntegerField(default=0)
    date_obtention = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Récompense pour {self.conducteur.user.email}: {self.description}"


class Paiement(models.Model):
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE, related_name='paiement')
    montant = models.DecimalField(max_digits=8, decimal_places=2)
    date_paiement = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=[
        ('EN_ATTENTE', 'En attente'),
        ('EFFECTUE', 'Effectué'),
        ('REMBOURSE', 'Remboursé')
    ], default='EN_ATTENTE')

    def __str__(self):
        return f"Paiement de {self.montant}€ pour la réservation {self.reservation}"
