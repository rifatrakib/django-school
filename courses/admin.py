from django.contrib import admin

from .models import Course, Instructor, Enrollment


class CourseAdmin(admin.ModelAdmin):
    ordering = ('code',)
    search_fields = ('title', 'code')
    list_display = ('title', 'code', 'credit')
    list_filter = ('credit',)


class InstructorAdmin(admin.ModelAdmin):
    ordering = ('course', 'teacher')
    search_fields = ('course', 'teacher')
    list_display = ('course', 'teacher', 'about')
    list_filter = ('course', 'teacher')


class EnrollmentAdmin(admin.ModelAdmin):
    ordering = ('course', 'student')
    search_fields = ('course', 'student')
    list_display = ('course', 'student', 'semester',
                    'score', 'grade', 'status')
    list_filter = ('course', 'student', 'semester', 'grade', 'status')


admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
