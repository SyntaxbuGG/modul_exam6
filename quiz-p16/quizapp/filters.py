from django_filters import FilterSet, CharFilter, NumberFilter
from django import forms
from django.contrib.auth import get_user_model

from quizapp.models import Result

User = get_user_model()

class TotalFilter(FilterSet):
    total = NumberFilter(
        field_name='total',
        lookup_expr='gt',
        label='Total Search',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    user__first_name = CharFilter(
        field_name='user__first_name',
        lookup_expr='icontains',
        label='Firstname Search',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    user__last_name = CharFilter(
        field_name='user__last_name',
        lookup_expr='icontains',
        label='Lastname Search',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Result
        fields = ['total', 'user__first_name', 'user__last_name']
