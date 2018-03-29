from django.contrib import admin
from django.contrib.auth.admin import (
    UserAdmin as BaseUserAdmin
)
from django.utils.translation import (
    gettext,
    gettext_lazy as _,
)
from .models import (
    User,
    Gender,
)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'email',
        'gender',
    )

    readonly_fields = (
        'last_login',
        'username',
        'date_joined',
    )

    fieldsets = (
        (
            _('Personal info'),
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'email',
                    'gender',
                )
            }
        ),
        (
            _('User info'),
            {
                'classes': (
                    'collapse',
                ),
                'fields': (
                    'username',
                    'password',
                )
            }
        ),
        (
            _('Permissions'),
            {
                'classes': (
                    'collapse',
                ),
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                )
            }
        ),
        (
            _('Important dates'),
            {
                'classes': (
                    'collapse',
                ),
                'fields': (
                    'last_login',
                    'date_joined',
                )
            }
        ),
    )


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    '''Admin View for Gender'''

    list_display = (
        'id',
        'gender',
        'referered_as',
    )
    search_fields = (
        'gender',
        'referered_as',
    )
