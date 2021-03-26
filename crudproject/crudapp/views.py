from django.shortcuts import render,HttpResponseRedirect
from .forms import UserRegistration
from .models import User


#For Add and Show
def add_show(request):

    if request.method == 'POST':
        fm = UserRegistration(request.POST)
        if fm.is_valid():
            fm.save()
        fm = UserRegistration()
    else:
        fm = UserRegistration()
    user = User.objects.all()

    return render(request,'crudapp/addshow.html',{'form':fm,'ur':user})


#For Update

def update(request,id):
    if request.method == 'POST':
        ui = User.objects.get(pk=id)
        fm = UserRegistration(request.POST,instance=ui)
        if fm.is_valid():
            fm.save()
        else:
            ui = User.objects.get(pk=id)
            fm = UserRegistration(instance=ui)
    else:
        fm = UserRegistration()
    return render(request,'crudapp/update.html',{'form':fm})
    
    

#For Delete

def delete(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')



