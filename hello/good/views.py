from django.shortcuts import render,HttpResponse
from datetime import datetime 
from good.models import Contact
from good.models import Register
from good.models import products
from good.models import categ

def index(request):
    prod=products.objects.all()
    
    return render(request, 'index1.html',{'pr':prod})


def contact(request):
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        contact = Contact(name=name,email=email,phone=phone,date=datetime.today())
        contact.save()
    return render(request, 'contact.html')
    

def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        register = Register(name=name,email=email,phone=phone)
        register.save()
    return render(request, 'register.html')


