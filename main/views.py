from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *


from .models import *
from django.db.models import Sum

from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
from .models import *

from datetime import date

from datetime import datetime
from django.urls import reverse
from django.http.response import HttpResponseRedirect, JsonResponse
from django.contrib import messages




from django.core.paginator import Paginator, EmptyPage

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




@login_required(login_url='login')
def view_customer(request):

    customer_id = request.POST.get('customer')

    customer_instance = customer.objects.get(id = customer_id)

    record_data = record.objects.filter(customer__id = customer_id)

    payment_data = payment.objects.filter(customer__id = customer_id).aggregate(payment_done_amount=Sum('amount'))["payment_done_amount"] or 0
    amo = record_data.aggregate(amo=Sum('amount'))["amo"] or 0
    outstaning_amount = amo - payment_data
    context = {
        'record_data': record_data,
        'amo': amo,
        'outstaning_amount': outstaning_amount,
        'customer_id': customer_id,
        'customer_instance' : customer_instance
    }

    return render(request, 'view_customer.html', context)


@login_required(login_url='login')
def view_customer_payment(request, customer_id):

    record_data = record.objects.filter(customer__id = customer_id).aggregate(payment_done_amount=Sum('amount'))["payment_done_amount"] or 0

    customer_instance = customer.objects.get(id = customer_id)

    payment_data = payment.objects.filter(customer__id = customer_id)
    total_payment = payment_data.aggregate(total_payment=Sum('amount'))["total_payment"] or 0
    
    total_outstanding = record_data - total_payment

    context = {
        'payment_data': payment_data,
        'total_payment': total_payment,
        'customer_id': customer_id,
        'total_outstanding': total_outstanding,
        'customer_instance': customer_instance,
    }

    return render(request, 'view_customer_payment.html', context)



from .filters import *

@login_required(login_url='login')
def list_record(request):


    records = record.objects.all()
    
    record_filters = record_filter(request.GET, queryset=records)
    
    filter_data = record_filters.qs


   

    page = request.GET.get('page', 1)
    paginator = Paginator(filter_data, 20)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    context = {
        'record_filters': record_filters,
        'data': data,
    }

    return render(request, 'list_record.html', context)


@login_required(login_url='login')
def list_payment(request):

    payments = payment.objects.all()

    payment_filters = payment_filter(request.GET, queryset=payments)
    
    filter_data = payment_filters.qs


   

    page = request.GET.get('page', 1)
    paginator = Paginator(filter_data, 20)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    context = {
        'payment_filters': payment_filters,
        'data': data,
    }

    return render(request, 'list_payment.html', context)




@login_required(login_url='login')
def view_customer_with_id(request, customer_id):

    
    record_data = record.objects.filter(customer__id = customer_id)
    
    customer_instance = customer.objects.get(id = customer_id)

    payment_data = payment.objects.filter(customer__id = customer_id).aggregate(payment_done_amount=Sum('amount'))["payment_done_amount"] or 0
    amo = record_data.aggregate(amo=Sum('amount'))["amo"] or 0
    outstaning_amount = amo - payment_data
    context = {
        'record_data': record_data,
        'amo': amo,
        'outstaning_amount': outstaning_amount,
        'customer_id': customer_id,
        'customer_instance': customer_instance,

    }

    return render(request, 'view_customer.html', context)




@login_required(login_url='login')
def add_customer(request):

    if request.method == 'POST':

        forms = customer_Form(request.POST)

        if forms.is_valid():
            
           
            forms.save()
        
            return redirect('dashboard')
        
        else:
            print(forms.errors)
    
    else:

        forms = customer_Form()

        context = {
            'form': forms
        }
        return render(request, 'add_customer.html', context)




@login_required(login_url='login')
def update_customer(request, customer_id):

    customer_instance = customer.objects.get(id = customer_id)

    if request.method == 'POST':

        forms = customer_Form(request.POST, instance = customer_instance)

        if forms.is_valid():
            
           
            forms.save()
        
            return redirect('list_customer')
        
        else:
            print(forms.errors)
    
    else:

        forms = customer_Form(instance=customer_instance)

        context = {
            'form': forms
        }
        return render(request, 'add_customer.html', context)





@login_required(login_url='login')
def list_customer(request):

    data = customer.objects.all()

    context = {
        'data': data
    }

    return render(request, 'list_customer.html', context)



@login_required(login_url='login')
def delete_customer(request, customer_id):

    customer.objects.get(id = customer_id).delete()

    return redirect('list_customer')






@login_required(login_url='login')
def add_test_type(request):

    if request.method == 'POST':

        forms = test_type_Form(request.POST)

        if forms.is_valid():
            
           
            forms.save()
        
            return redirect('list_test_type')
        
        else:
            print(forms.errors)
    
    else:

        forms = test_type_Form()

        context = {
            'form': forms
        }
        return render(request, 'add_test_type.html', context)




@login_required(login_url='login')
def update_test_type(request, test_type_id):

    test_type_instance = test_type.objects.get(id = test_type_id)

    if request.method == 'POST':

        forms = test_type_Form(request.POST, instance = test_type_instance)

        if forms.is_valid():
            
           
            forms.save()
        
            return redirect('list_test_type')
        
        else:
            print(forms.errors)
    
    else:

        forms = test_type_Form(instance=test_type_instance)

        context = {
            'form': forms
        }
        return render(request, 'add_test_type.html', context)





@login_required(login_url='login')
def list_test_type(request):

    data = test_type.objects.all()

    context = {
        'data': data
    }

    return render(request, 'list_test_type.html', context)



@login_required(login_url='login')
def delete_test_type(request, test_type_id):

    test_type.objects.get(id = test_type_id).delete()

    return redirect('list_test_type')






@login_required(login_url='login')
def add_record(request, customer_id):

    customer_instance = customer.objects.get(id = customer_id)

    if request.method == 'POST':

        forms = record_Form(request.POST)

        if forms.is_valid():
            
           
            forms.save()
        
            return redirect(reverse('view_customer_with_id', args=[customer_id]))
        
        else:
            print(forms.errors)
    
    else:

        forms = record_Form()

        context = {
            'form': forms,
            'customer' : customer_id,
            'customer_instance' : customer_instance,
        }
        return render(request, 'add_record.html', context)


@login_required(login_url='login')
def update_record(request, record_id):


    record_instance = record.objects.get(id = record_id)

    customer_instance = record_instance.customer

    if request.method == 'POST':

        forms = record_Form(request.POST, instance = record_instance)

        if forms.is_valid():
            
           
            forms.save()
        
            return redirect(reverse('view_customer_with_id', args=[customer_instance.id]))
        
        else:
            print(forms.errors)
    
    else:

        forms = record_Form(instance = record_instance)

        context = {
            'form': forms,
            'customer' : customer_instance.id,
            'customer_instance' : customer_instance,
        }
        return render(request, 'add_record.html', context)




import copy


@login_required(login_url='login')
def delete_record(request, record_id):

    data = record.objects.get(id = record_id)

    record_instance = copy.copy(data)

    data.delete()

    return redirect(reverse('view_customer_with_id', args=[record_instance.customer.id]))




# def add_payment(request):

#     if request.method == 'POST':


@login_required(login_url='login')
def add_payment(request, customer_id):

    customer_instance = customer.objects.get(id = customer_id)

    if request.method == 'POST':


            
        updated_request = request.POST.copy()
        updated_request.update({'customer': customer_instance.id})

        forms = payment_Form(updated_request)

        if forms.is_valid():
            
           
            forms.save()
        
        
            return redirect(reverse('view_customer_payment', args=[customer_id]))

        
        else:
            print(forms.errors)
    
    else:

        forms = payment_Form()

        data = payment.objects.filter(customer = customer_instance)

        total_paid = data.aggregate(Sum('amount'))['amount__sum'] or 0

        context = {
            'form': forms,
            'data': data,
            'customer_instance' : customer_instance,
            'total_paid' : total_paid,
        }
        return render(request, 'add_payment.html', context)
    


@login_required(login_url='login')
def update_payment(request, payment_id):

    payment_instance = payment.objects.get(id = payment_id)

    if request.method == 'POST':


            
        updated_request = request.POST.copy()
        updated_request.update({'customer': payment_instance.customer.id})

        forms = payment_Form(updated_request, instance = payment_instance)

        if forms.is_valid():
            
           
            forms.save()

            return redirect(reverse('view_customer_payment', args=[payment_instance.customer.id]))

        
        else:
            print(forms.errors)
    
    else:

        forms = payment_Form(instance = payment_instance)

        context = {
            'form': forms,
        }
        return render(request, 'update_payment.html', context)







@login_required(login_url='login')
def delete_payment(request, payment_id):

    data = payment.objects.get(id = payment_id)
    data_copy = copy.copy(data)
    data.delete()

    
    
    return redirect(reverse('view_customer_payment', args=[data_copy.customer.id]))


