from django.shortcuts import render

from courses.models import Instructor, Enrollment


def dashboard(request):
    report_count = 0
    course_count = Instructor.objects.filter(
        teacher__teacher=request.user
    ).count()
    student_count = Enrollment.objects.filter(
        course__teacher__teacher=request.user
    ).count()
    context = {
        'report_count': report_count,
        'course_count': course_count,
        'student_count': student_count,
    }
    return render(request, 'users/index.html', context)
