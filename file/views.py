from django.contrib.auth.signals import user_logged_in
from django.shortcuts import render,redirect
from django.contrib.auth import login as _login,authenticate, logout as _logout
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView
from django.contrib.auth import get_user_model
from file.models import user

 

@require_http_methods(["POST","GET"])
def login(request):
    if request.method=="GET":
        return render(request,"file/login.html")
    else:
        username=request.POST.get("username","")
        password=request.POST.get("password","")
        user1=authenticate(request,username=username,password=password)
        print(user1,"user")
        if user1 is not None:
            _login(request,user1)
            return redirect('base')
        else:
            return redirect('files:login')


def logout(request):
    _logout(request)
    return redirect('base')


def register(request):
    if request.method=="GET":
        return render(request,"file/register.html")
    else:
        username=request.POST.get("username","")
        password=request.POST.get("password","")
        repassword=request.POST.get("repassword","")

    if password==repassword:
        if user.objects.filter(username=username).exists():
            return render(request,"file/register.html",{"error":"username vojud darad"})
        else:
            try:
                user1=user(username=username)
                user1.set_password(password)
                user1.save()
                _login(request,user1)
                return redirect('base')
            except Exception:
                return render(request,"file/register.html",{"error":"ba arze puzesh dobare say konid"})

    else:
        return render(request,"file/register.html",{"error":"password ro mesle ham vared kon"})




def show_files(request):
    # model=user
    # query=user.objects.
    # context_object_name="user_files"
    # template_name="file/files.html"
   
    qs=user.objects.get(username=request.user)
    files=qs.file.path
    ctx={"files":files}
    return render(request,"file/file.html",ctx)

