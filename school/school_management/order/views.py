from django.shortcuts import render
from django.shortcuts import render,redirect
from .forms import OrderForm
from .models import Order
from .models import Course
from django.contrib.auth.decorators import login_required
from django .contrib import messages,auth
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404


@login_required(login_url='login')
def place_orders(request):
    
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('place_order')
    return render(request, 'order.html', {'form': form})

    # if request.method == 'POST':
    #     form =OrderForm(request.POST)
        
    #     if form.is_valid():
                        
    #         form.save()

    #         messages.error(request,'Order Confirmed') 
    #         form = OrderForm()
    #         context = { 'form' : form, 'order' :True } 
    #         return render(request,'order.html',context) 
    #     else:
    #         form =OrderForm(request.POST)
    #         context = { 'form' : form, 'order' :False } 
    #         messages.error(request,'OrderNot Confirmed') 
    #         return render(request,'order.html',context)

    # form =OrderForm()
    # context = { 'form' : form }
    # return render(request,'order.html',context)

# def person_update_view(request, pk):
#     person = get_object_or_404(Order, pk=pk)
#     form = OrderForm(instance=person)
#     if request.method == 'POST':
#         form = OrderForm(request.POST, instance=person)
#         if form.is_valid():
#             form.save()
#             return redirect('person_change', pk=pk)
#     return render(request, 'order.html', {'form': form})    


# AJAX
def load_course(request):
    department_id = request.GET.get('department_id')
    course = Course.objects.filter(department_id=department_id).all()
    # return render(request, 'city_dropdown_list.html', {'course': course})
    return JsonResponse(list(course.values('id', 'name')), safe=False)   