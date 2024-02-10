from django.shortcuts import render,redirect
from django.views.generic import View,ListView,DetailView,CreateView
from .models import categories,bestsellers,products
from kyra_app.forms import register,loginform
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
import sqlite3
from django.contrib import messages




class home(ListView):
   model=bestsellers
   template_name="index.html"
   context_object_name="bestseller"
    
   

class registerview(View):
  def get(self,request,*args,**kwargs):
    form=register()
    return render(request,"reg.html",{"form":form})


  def post(self,request,*args,**kwargs):
    form=register(request.POST)
    if form.is_valid():
      User.objects.create_user(**form.cleaned_data)
      messages.success(request,"user registerd successfully")
      form.save()
    else:
     messages.error(request,"user registration failed")
     print("get out")
    return render(request,"reg.html",{"form":form})

class loginview(View):
    def get(self,request,*args,**kwargs):
        form=loginform
        return render(request,"login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=loginform(request.POST)
        if form.is_valid():
            u_name=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_obj=authenticate(request,username=u_name,password=pwd)
            if user_obj:
                login(request,user_obj)
                return redirect("home")
            else:
                print('false')
            return redirect("home")
        
class productsview(View):
   def get(self,request,*args,**kwargs):
      id=kwargs.get("pk")      
      data=products.objects.filter(category_id=id)
      name=categories.objects.get(id=id)
      return render(request,"products.html",{"data":data})
   
class product_detail(View):
   def get(self,request,*args,**kwargs):
      id=kwargs.get("pk")
      p_data=products.objects.filter(id=id)
      return render(request,"p_details.html",{"p_data:"p_data})
