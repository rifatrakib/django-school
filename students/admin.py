from django.contrib import admin

from .models import Student


class StudentAdmin(admin.ModelAdmin):
    ordering = ('-started_on', 'identity')


admin.site.register(Student, StudentAdmin)
