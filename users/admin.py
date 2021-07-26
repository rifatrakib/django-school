from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm

    search_fields = (
        'email', 'first_name', 'last_name',
        'phone_number', 'username')
    ordering = ('username',)
    list_filter = ('sex', 'role', 'birthday', 'date_joined')

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Additional Information', {'fields': (
                'sex', 'role', 'birthday', 'phone_number', 'bio', 'avatar')}
        )
    )


admin.site.register(CustomUser, CustomUserAdmin)
