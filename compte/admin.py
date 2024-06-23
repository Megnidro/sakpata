from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [ 'role', 'phone_number', 'email_notifications']
    list_filter = ['role']
    search_fields = ['user__email', 'phone_number']
    readonly_fields = ['total_trips_offered', 'total_trips_taken']


class CustomUserAdmin(UserAdmin):
    model = Profile
    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'is_superuser']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_superuser'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


# Register your custom admin class with the built-in UserAdmin
admin.site.register(Profile, CustomUserAdmin)
