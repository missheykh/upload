from django.shortcuts import render

def base(request):
    ctn={}
    return render(request,"base.html",ctn)


    