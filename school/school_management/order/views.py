from django.shortcuts import render
from django.shortcuts import render,redirect
from .forms import OrderForm
from .models import Order
from django.contrib.auth.decorators import login_required
from django .contrib import messages,auth


@login_required(login_url='login')
def place_orders(request):

    if request.method == 'POST':
        form =OrderForm(request.POST)
        
        if form.is_valid():
        
            data = Order()
            
            data.name = form.cleaned_data['name']
            data.mobile = form.cleaned_data['mobile']
            data.email = form.cleaned_data['email']
            data.address = form.cleaned_data['address']
            data.age = form.cleaned_data['age']
            data.gender = form.cleaned_data['gender']
            data.date_of_birth= form.cleaned_data['date_of_birth']
            data.course = form.cleaned_data['course']
            data.purpose = form.cleaned_data['purpose']
            data.materials = form.cleaned_data['materials']
            data.save()
            messages.error(request,'Order Confirmed') 
            form = OrderForm()
            context = { 'form' : form }
            return render(request,'order.html',context) 

    form =OrderForm()
    context = { 'form' : form }
    return render(request,'order.html',context)