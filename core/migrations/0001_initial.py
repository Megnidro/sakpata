# Generated by Django 5.0.6 on 2024-06-23 09:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('color', models.CharField(max_length=30)),
                ('license_plate', models.CharField(max_length=20)),
                ('seats', models.IntegerField(default=4)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_places', models.IntegerField(default=1)),
                ('statut', models.CharField(choices=[('EN_ATTENTE', 'En attente'), ('CONFIRMEE', 'Confirmée'), ('ANNULEE', 'Annulée')], default='EN_ATTENTE', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.DecimalField(decimal_places=2, max_digits=8)),
                ('date_paiement', models.DateTimeField(auto_now_add=True)),
                ('statut', models.CharField(choices=[('EN_ATTENTE', 'En attente'), ('EFFECTUE', 'Effectué'), ('REMBOURSE', 'Remboursé')], default='EN_ATTENTE', max_length=20)),
                ('reservation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='paiement', to='core.reservation')),
            ],
        ),
        migrations.CreateModel(
            name='Trajet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depart', models.CharField(max_length=100)),
                ('arrivee', models.CharField(max_length=100)),
                ('date_depart', models.DateTimeField()),
                ('places_disponibles', models.IntegerField(default=1)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=8)),
                ('voiture', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.car')),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='trajet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='core.trajet'),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('role', models.CharField(choices=[('passager', 'passager'), ('driver', 'conducteur'), ('alternant', 'alternant')], default='passager', max_length=10)),
                ('smoker', models.BooleanField(default=False)),
                ('pets_allowed', models.BooleanField(default=False)),
                ('music_preferences', models.CharField(blank=True, max_length=100, null=True)),
                ('chat_preferences', models.CharField(blank=True, max_length=100, null=True)),
                ('total_trips_offered', models.IntegerField(default=0)),
                ('total_trips_taken', models.IntegerField(default=0)),
                ('email_notifications', models.BooleanField(default=True)),
                ('sms_notifications', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='trajet',
            name='conducteur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trajets_proposes', to='core.userprofile'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='passager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='core.userprofile'),
        ),
        migrations.CreateModel(
            name='Recompense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('points', models.IntegerField(default=0)),
                ('date_obtention', models.DateTimeField(auto_now_add=True)),
                ('conducteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recompenses', to='core.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Reclamation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('statut', models.CharField(choices=[('OUVERTE', 'Ouverte'), ('EN_COURS', 'En cours de traitement'), ('RESOLUE', 'Résolue'), ('FERMEE', 'Fermée')], default='OUVERTE', max_length=20)),
                ('trajet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reclamations', to='core.trajet')),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reclamations', to='core.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.TextField()),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('lue', models.BooleanField(default=False)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('destinataire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='core.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='core.userprofile'),
        ),
        migrations.CreateModel(
            name='DriverRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(default=0.0)),
                ('comment', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings_received', to='core.userprofile')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings_given', to='core.userprofile')),
            ],
            options={
                'unique_together': {('driver', 'passenger')},
            },
        ),
    ]
