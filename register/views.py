from django.shortcuts import render
from .forms import RegisterForm
def register(response):
    form = RegisterForm()
    if response.method=="POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
    else:
            form = RegisterForm()    
    return render(response,'register/register.html',{'form':form})