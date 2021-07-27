from django.contrib import admin

from .models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    ordering = ('-started_on',)
    list_display = ('username', 'teacher', 'phone_number',
                    'gender', 'started_on')
    list_filter = ('started_on',)


admin.site.register(Teacher, TeacherAdmin)
