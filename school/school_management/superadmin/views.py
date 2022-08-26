from django.shortcuts import render


from django.shortcuts import redirect, render
from django.contrib import messages, auth
from Department.forms import DepartmentForm,CourseForm,MaterialForm
from Account.models import Account
from django.contrib.auth.decorators import login_required
from order.models import Order     
from django.views.decorators.cache import never_cache
from django.contrib.auth import logout


def master_signin(request):
    if request.user.is_authenticated:
        return redirect("admin_home")

    if request.method == "POST":

        email = request.POST["email"]
        password = request.POST["password"]
        try:
            user = Account.objects.get(email=email, is_admin=True)
        except :
            messages.error(request,"admin does not exist")    
            return redirect("admin_signin")



        # email = request.POST["email"]
        # password = request.POST["password"]
        user = auth.authenticate(email=email,password=password,is_admin=True)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Login Successful")
            return redirect("admin_home")
        else:
            messages.error(request, "Invalid credentials")
            return redirect("admin_signin")

    else:
        return render(request, "admin_login.html")

@login_required(login_url='admin_signin')
def admin_home(request):

    return render (request,'admin/admindash.html')


@login_required(login_url='admin_signin')
def customer(request):
    users = Account.objects.all()
    context = {"users": users}
    return render(request, "admin/customer.html", context)


@login_required(login_url='admin_signin')
def customer_pickoff(request, customer_id):
    customer = Account.objects.get(pk=customer_id)
    if customer.is_active:
        customer.is_active = False
        
    else:
        customer.is_active = True
    customer.save()

    return redirect("customer")    



@login_required(login_url='admin_signin')
def add_department(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST,request.FILES)
        if form.is_valid():
            print('valid')
            form.save()
            print('data saved successfully')
            return redirect('add_department')
        else:
            print('product not added')
            messages.info(request,'product not added')
    else:
        form = DepartmentForm()
    return render(request,"add_product.html",{'form':form})



def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST,request.FILES)
        if form.is_valid():
            print('valid')
            form.save()
            print('data saved successfully')
            return redirect('add_course')
        else:
            print('product not added')
            messages.info(request,'product not added')
    else:
        form = CourseForm()
    return render(request,"add_product.html",{'form':form})

def add_Material(request):
    if request.method == "POST":
        form = MaterialForm(request.POST,request.FILES)
        if form.is_valid():
            print('valid')
            form.save()
            print('data saved successfully')
            return redirect('add_Material')
    
    form = MaterialForm()
    return render(request,"add_product.html",{'form':form})
    
@login_required(login_url='admin_signin')
def order_details(request):
    order= Order.objects.all()
    context = {'order':order}
    return render(request,'admin/billing.html',context)


@never_cache
def admin_logouts(request):

    auth.logout(request)
    return redirect(master_signin)    