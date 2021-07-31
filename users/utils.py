from students.models import Student

from io import BytesIO

import base64
import matplotlib.pyplot as plt
import seaborn as sns


def get_image():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def generate_chart_image(chart_type, *args, **kwargs):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(10, 5))
    data = kwargs.get('data')
    if chart_type == 'Bar Chart':
        sns.barplot(x=data['student'], y=data['score'], data=data['score'])
    plt.tight_layout()
    chart = get_image()
    return chart


def get_student_name(value):
    student = Student.objects.get(student_id=value)
    return student.__str__()
