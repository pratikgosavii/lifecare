from django import forms

from .models import *
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from django.forms.widgets import DateTimeInput

        


class customer_Form(forms.ModelForm):
    class Meta:
        model = customer
        fields = '__all__'
        widgets = {
           
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'mobile': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'mobile'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'random_key'
            }),
            

        }

class test_type_Form(forms.ModelForm):
    class Meta:
        model = test_type
        fields = '__all__'
        widgets = {
           
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            

        }

class record_Form(forms.ModelForm):
    class Meta:
        model = record
        fields = '__all__'
        widgets = {
           
            'customer': forms.Select(attrs={
                'class': 'form-control', 'id': 'customer'
            }),
            'test_type': forms.Select(attrs={
                'class': 'form-control', 'id': 'test_type'
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'amount'
            }),
            'remark': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'random_key'
            }),
            'dr': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'random_key'
            }),

            'date': DateTimeInput(attrs={'type': 'date', 'class' : 'form-control'}, format = '%Y-%m-%d'),


        }

class payment_Form(forms.ModelForm):
    class Meta:
        model = payment
        fields = '__all__'
        widgets = {
           
           'customer': forms.Select(attrs={
                'class': 'form-control', 'id': 'customer'
            }),
            'demo': forms.Select(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'amount': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'amount'
            }),
            'remark': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'random_key'
            }),

            'date': DateTimeInput(attrs={'type': 'date', 'class' : 'form-control'}, format = '%Y-%m-%d'),


        }

