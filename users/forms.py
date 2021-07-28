from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


CHARTS = (
    ('Bar Chart', 'Individual Scores'),
    ('Line Chart', 'Academic Growth'),
    ('Scatterplot', 'Gender-wise Scores'),
)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = '__all__'


class ChartSelectionForm(forms.Form):
    chart = forms.ChoiceField(
        choices=CHARTS,
        widget=forms.Select(attrs={
            'class': 'form-control mb-2',
        })
    )
    start = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Input semester from which result to be analyzed'
        })
    )
    last = forms.IntegerField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Input semester upto which result to be analyzed',
        })
    )
