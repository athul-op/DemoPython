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
                        
            form.save()

            messages.error(request,'Order Confirmed') 
            form = OrderForm()
            context = { 'form' : form, 'order' :True } 
            return render(request,'order.html',context) 
        else:
            form =OrderForm(request.POST)
            context = { 'form' : form, 'order' :False } 
            messages.error(request,'OrderNot Confirmed') 
            return render(request,'order.html',context)

    form =OrderForm()
    context = { 'form' : form }
    return render(request,'order.html',context)