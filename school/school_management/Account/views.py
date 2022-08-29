from django.shortcuts import render

# Create your views here.
from.models import Account
from . forms import  RegistrationForm
from django .contrib import messages,auth
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth import authenticate,logout

def register(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        print('form created')


        if form.is_valid():
            print('form valid')
            username = form.cleaned_data['username']
            email    = form.cleaned_data['email']
            mobile   = form.cleaned_data['mobile']
            password = form.cleaned_data['password']

            print(username,email)

            user = Account.objects.create_user(
                username=username,
                email     =email,
                mobile    =mobile,
                password  =password,
            )
            user.save()
            messages.error(request,'user  create') 
            
            return redirect(user_login)
        else:    
            messages.error(request,'user does not create')  

    form = RegistrationForm()
    context = { 'form' : form }
    return render(request,'signup.html',context)  



def user_login(request):

    if request.user.is_authenticated:
       return redirect('home')

    if request.method == 'POST':


        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
           user = Account.objects.get(email=email)
        except:
            messages.error(request,"user does not exist..")
            return redirect('login')
        if  user.is_active:
            user = authenticate(request,email=email,password=password)
            if user is not None:
               auth.login(request,user)
               return redirect('home')
            else:
               messages.error(request,'user does not exit')

        else:
            messages.error(request,'you have been blocked by admin') 
            return redirect('login')   
    return render(request,'login.html')


def home(request):
    return render(request,'index.html')



def user_logout(request):
    auth.logout(request)
    return redirect('home')     