from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from .models import *

class MaqolaView(View):
    def get(self,request):
        m=Maqola.objects.all()
        return render(request,"maqola.html",{"maqola":m})
    def post(self,request):
        m=Muallif.objects.get(user=request.user)
        Maqola.objects.create(
            sarlavha=request.POST.get('s'),
            sana=request.POST.get('sana'),
            mavzu=request.POST.get('m'),
            matn=request.POST.get('matn'),
            muallif=m
        )
        return redirect("")
class KirishView(View):
    def get(self, request):
        return render(request, "kirish.html")
    def post(self, request):
        l = request.POST.get("l")
        p = request.POST.get("p")
        userlar = authenticate(request, username=l, password=p)
        if userlar is None:
            return redirect("login")
        login(request, userlar)
        return redirect("maqola")
class LoginView(View):
    def get(self,request):
        return render(request,"register.html")
    def post(self,request):
        u=User.objects.create_user(
            username=request.POST.get('u'),
            password=request.POST.get('p')
        )
        m=Muallif.objects.create(
            ism=request.POST.get('i'),
            tugulgan_sana=request.POST.get('t'),
            maqolalar_soni=request.POST.get('m'),
            user=u
        )
        return redirect("kirish")
class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("kirish")