from django.contrib import admin

from .models import Student


class StudentAdmin(admin.ModelAdmin):
    ordering = ('-started_on',)
    list_display = ('username', 'student', 'phone_number',
                    'gender', 'started_on')
    list_filter = ('started_on',)


admin.site.register(Student, StudentAdmin)
