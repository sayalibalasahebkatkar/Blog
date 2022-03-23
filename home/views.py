from click import password_option
from django.http import HttpResponse
from django.shortcuts import redirect, render
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def home(request):
    return render(request,'home/home.html')

def contact(request):       
    messages.debug(request,'welcome to contact debug')

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request,'home/contact.html')

def handlesignup(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['cpassword']

        # check errors if any
        if len(username)>10:
            messages.error(request,'Username must be under 10 characters')
            return redirect('home')
        
        user1=User.objects.filter(username=username)
        if user1:
            # print(user1)
            messages.error(request,'Username exists!!')
            return redirect('home')

        if password!=password2:
            messages.error(request,'Passwords do not match')
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request,'Username should only contains Letters and Number')
            return redirect('home')

        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=fname
        myuser.last_name=lname

        #Save User
        myuser.save()
        messages.success(request,'Your account has been created successfully!!')
        
        return redirect('home')
    else:
        return HttpResponse('404 - Not Found')

def handlelogin(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        password = request.POST['pass']
        user=authenticate(username=loginusername,password=password)
        if user is not None:
            print(user)
            login(request,user)
            messages.success(request,'Successfully logged In!!')
            
        else:
            messages.error(request,'Incorrect credentials')
        return redirect('home')
    else:
        return redirect('home')


def handlelogout(request):
    print(request)
    logout(request)
    messages.success(request,"Successfully logged Out!!")
    return redirect('handlelogin')  

def about(request):
    return render(request,'home/about.html')
