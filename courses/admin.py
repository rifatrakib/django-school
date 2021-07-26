from django.contrib import admin

from .models import Course


class CourseAdmin(admin.ModelAdmin):
    ordering = ('code',)


admin.site.register(Course, CourseAdmin)
