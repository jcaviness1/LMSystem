from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import CustomUser


class CustomUserAdmin(DefaultUserAdmin):
   
    fieldsets = (
        (None, {'fields': ('username', 'password')}),  # Login details
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),  # Personal details
        ('Roles', {'fields': ('is_student', 'is_teacher', 'is_admin')}),  # Role fields
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_authorized',  # Add is_authorized here
                                    'groups', 'user_permissions')}),  # Admin permissions
    )

   
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_authorized', 'is_student', 'is_teacher', 'is_admin')}
         ),
    )

   
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_authorized',
        'is_student', 'is_teacher', 'is_admin', 'is_staff', 'is_superuser'
    )

   
    list_filter = ('is_student', 'is_teacher', 'is_admin', 'is_authorized', 'is_staff', 'is_superuser')

   
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset  # Superusers see all users
        return queryset.filter(is_superuser=True)  # Non-superuser staff won't see superusers


admin.site.register(CustomUser, CustomUserAdmin)