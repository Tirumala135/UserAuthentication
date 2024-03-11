from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth import login
from django.views import View

# Create your views here.

class Registration_Views(View):
    def get(self,request):
        register=RegistrationForm()
        return render(request,'Registration/Register.html',{'forms':register})
    def post(self,request):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('/')
        return render(request,'Registration/Register.html',{'forms':form})
