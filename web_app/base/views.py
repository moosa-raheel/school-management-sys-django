from django.shortcuts import render
from base.forms import Registration_form,Login_form
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
# Ye Login Authentiation Ka code he
def login__sys(request):
    # Login Checking
    if request.user.is_authenticated:
        return HttpResponseRedirect("/dashboard")
    else:
        if request.method == "POST":
            fm = Login_form(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data.get("username")
                upass = fm.cleaned_data.get("password")
                user = authenticate(username=uname,password=upass)
                if user:
                    login(request,user)
                    return HttpResponseRedirect("/dashboard")
        else:
            fm = Login_form()
        return render(request,"login.html",{"form":fm})
    
# Sun be ye signup ka code he smjha
def signup_sys(request):
    #Login Checking
    if request.user.is_authenticated:
        return HttpResponseRedirect("/dashboard")
    else:
        if request.method == "POST":
            fm = Registration_form(request.POST)
            if fm.is_valid():
                fm.save()
                return HttpResponseRedirect("/login")
        else:
            fm = Registration_form()
        fm.label_suffix = ""
        return render(request,"signup.html",{"form":fm})
    
def dashboard_page(request):
    if request.user.is_authenticated:
        return render(request,"dashboard.html")
    else:
        return HttpResponseRedirect("/login")
    
def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/login")