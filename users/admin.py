from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Profile
from .forms import CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm

    search_fields = (
        'email', 'first_name', 'last_name',
        'phone_number', 'username')
    ordering = ('username',)
    list_filter = ('sex', 'role', 'birthday', 'date_joined')
    list_display = ('username', '__str__', 'email', 'role', 'sex', 'is_staff')

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Additional Information', {'fields': (
                'sex', 'role', 'birthday', 'phone_number', 'bio', 'avatar')}
        )
    )


class ProfileAdmin(admin.ModelAdmin):
    ordering = ('owner',)
    list_display = ('username', 'owner', 'gender',
                    'phone_number', 'start_date', 'address')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)
