from django.contrib import admin
from .models import UserProfile, Car, DriverRating, Trajet, Reservation, Reclamation, Notification, Recompense, Paiement


# Register your models here.


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['owner', 'make', 'model', 'year']
    search_fields = ['owner__user__email', 'make', 'model']


@admin.register(DriverRating)
class DriverRatingAdmin(admin.ModelAdmin):
    list_display = ['driver', 'passenger', 'rating', 'date']
    search_fields = ['driver__user__email', 'passenger__user__email']
    list_filter = ['driver', 'passenger']


@admin.register(Trajet)
class TrajetAdmin(admin.ModelAdmin):
    list_display = ['conducteur', 'depart', 'arrivee', 'date_depart', 'places_disponibles']
    list_filter = ['conducteur']
    search_fields = ['conducteur__user__email', 'depart', 'arrivee']


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['trajet', 'passager', 'nombre_places', 'statut']
    list_filter = ['statut']
    search_fields = ['trajet__depart', 'trajet__arrivee', 'passager__user__email']


@admin.register(Reclamation)
class ReclamationAdmin(admin.ModelAdmin):
    list_display = ['auteur', 'trajet', 'date_creation', 'statut']
    list_filter = ['statut']
    search_fields = ['auteur__user__email', 'trajet__depart', 'trajet__arrivee']


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['destinataire', 'contenu', 'date_creation', 'lue']
    list_filter = ['destinataire']
    search_fields = ['destinataire__user__email', 'contenu']


@admin.register(Recompense)
class RecompenseAdmin(admin.ModelAdmin):
    list_display = ['conducteur', 'description', 'points', 'date_obtention']
    search_fields = ['conducteur__user__email', 'description']
    list_filter = ['points']


@admin.register(Paiement)
class PaiementAdmin(admin.ModelAdmin):
    list_display = ['reservation', 'montant', 'date_paiement', 'statut']
    list_filter = ['statut']
    search_fields = ['reservation__trajet__depart', 'reservation__trajet__arrivee']
