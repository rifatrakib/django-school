from django.contrib import admin

from .models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    ordering = ('-started_on',)


admin.site.register(Teacher, TeacherAdmin)
