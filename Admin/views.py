from django.shortcuts import render

# Create your views here.
def Dashboard(request):
    return render(request,'Dashbord.html')
def admininfo(request):
    return render(request,'admin.html')


def department(request):
    return render(request,'departments.html')


def doctor(request):
    return render(request,'doctors.html')


def patients(request):
    return render(request,'patients.html')


def ticket(request):
    return render(request,'ticket.html')
    
    
    
    
