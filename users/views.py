from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum, Count

from .forms import ChartSelectionForm
from .utils import generate_chart_image, get_student_name

from courses.models import Instructor, Enrollment

import pandas as pd
import numpy as np


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
        # print(data)
        data = data.groupby('student_id', as_index=False)[['score']].sum()
        data['student_id'] = data['student_id'].apply(get_student_name)
        data.rename({'student_id': 'student'}, axis=1, inplace=True)
        chart = generate_chart_image(chart_type, data=data)
        average = np.mean(data['score'])
        std_deviation = np.std(data['score'])
        print(std_deviation)
        maximum = float(np.max(data['score']))
        minimum = float(np.min(data['score']))
        return JsonResponse({
            'chart': chart,
            'average': average,
            'maximum': maximum,
            'minimum': minimum,
            'std_deviation': std_deviation,
            # 'form': form,
            # 'data': data,
        })
    return JsonResponse({})
