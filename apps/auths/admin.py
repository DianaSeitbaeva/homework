from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import (
    CustomUserCreationForm,
    CustomUserChangeForm,
)
from auths.models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = (
        (
            None, {
                'fields': (
                    'email', 'password',
                ),
            }
        ),
        (
            'Permissions', {
                'fields': ('is_active',)
            }
        ),
    )
    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': (
                    'email', 'password1', 'password2', 'is_active',
                ),
            }
        ),
    )
    list_display = ('email', 'is_active',)
    list_filter = ('email', 'is_active',)
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(
    CustomUser, CustomUserAdmin
)