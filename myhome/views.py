from django.contrib import messages
from django.shortcuts import render, HttpResponse
from datetime import datetime
from myhome.models import Contacts

def index(request):
    messages.success(request,"this isatest message")

    return render(request, 'index.html')
    
def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')
    #return HttpResponse('this is service page')

def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contacts = Contacts(name= name, email= email, phone= phone, desc= desc, date= datetime.today())
        contacts.save()
        messages.success(request,'Your Request has been Sent')

    
    return render(request, 'contacts.html')
    # return HttpResponse('this is contact page')

# Create your views here.
