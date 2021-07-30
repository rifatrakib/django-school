from django.shortcuts import render

from .forms import ChartSelectionForm
from .utils import generate_chart_image

from courses.models import Instructor, Enrollment

import pandas as pd


def dashboard(request):
    report_count = 0
    course_count = Instructor.objects.filter(
        teacher__teacher=request.user
    ).count()
    student_count = Enrollment.objects.filter(
        course__teacher__teacher=request.user
    ).count()
    form = ChartSelectionForm()
    context = {
        'form': form,
        'report_count': report_count,
        'course_count': course_count,
        'student_count': student_count,
    }
    return render(request, 'users/index.html', context)


def process_chart(request):
    form = ChartSelectionForm(request.POST or None)
    if request.is_ajax():
        chart_type = request.POST.get('chartType')
        start = request.POST.get('start')
        last = request.POST.get('last')
        qs = Enrollment.objects.filter(
            semester__gte=start, semester__lte=last,
            course__teacher__teacher=request.user)
        data = pd.DataFrame(qs.values())
        # convert the course and student fields using apply method
