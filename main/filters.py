import django_filters
from django_filters import DateFilter, CharFilter
from django.forms.widgets import DateInput
from django import forms

from .models import *
from .forms import *




class record_filter(django_filters.FilterSet):

    customer = django_filters.ModelChoiceFilter(
        queryset=customer.objects.all(),
       widget=forms.Select(
            attrs={
                'class' : 'form-control sele',
                'id' : 'employee'
            })
    )

    from_date = DateFilter(
        field_name="date",  # Field name to filter on
        lookup_expr='gte',  # 'gte' means greater than or equal to
        widget=forms.DateInput(attrs={'id': 'from_datepicker', 'type': 'date', 'class': 'form-control date_css'}),
    )
    
    to_date = DateFilter(
        field_name="date",  # Field name to filter on
        lookup_expr='lte',  # 'lte' means less than or equal to
        widget=forms.DateInput(attrs={'id': 'to_datepicker', 'type': 'date', 'class': 'form-control date_css'}),
    )

    
    class Meta:
        model = record
        fields = '__all__'
       
   



class payment_filter(django_filters.FilterSet):

    customer = django_filters.ModelChoiceFilter(
        queryset=customer.objects.all(),
       widget=forms.Select(
            attrs={
                'class' : 'form-control sele',
                'id' : 'employee'
            })
    )

    from_date = DateFilter(
        field_name="date",  # Field name to filter on
        lookup_expr='gte',  # 'gte' means greater than or equal to
        widget=forms.DateInput(attrs={'id': 'from_datepicker', 'type': 'date', 'class': 'form-control date_css'}),
    )
    
    to_date = DateFilter(
        field_name="date",  # Field name to filter on
        lookup_expr='lte',  # 'lte' means less than or equal to
        widget=forms.DateInput(attrs={'id': 'to_datepicker', 'type': 'date', 'class': 'form-control date_css'}),
    )

    
    class Meta:
        model = payment
        fields = '__all__'
       
   

