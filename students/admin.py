from django.contrib import admin

from .models import Student


class StudentAdmin(admin.ModelAdmin):
    ordering = ('-started_on',)


admin.site.register(Student, StudentAdmin)
