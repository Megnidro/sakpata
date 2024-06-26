# Generated by Django 5.0.6 on 2024-06-23 12:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compte', '0002_alter_profile_is_active_alter_profile_is_staff_and_more'),
    ]

    operations = [
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
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
