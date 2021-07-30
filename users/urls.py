from django.urls import path

from .views import dashboard, process_chart


app_name = 'users'
urlpatterns = [
    path('', dashboard, name='index'),
    path('dashboard-chart/', process_chart, name='dashboard_chart'),
]
