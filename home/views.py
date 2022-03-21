from django.http import HttpResponse
from django.shortcuts import render
from home.models import Contact
from django.contrib import messages
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

def about(request):
    return render(request,'home/about.html')
