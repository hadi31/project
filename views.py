from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from accounts.models import *
from django.http import HttpResponse, JsonResponse
from django.http.response import HttpResponseRedirect



# Create your views here.


def userHomepage(request):
    if request.user.is_authenticated:
        check_id = request.user.id
        try:
            if application.objects.get(appID=check_id):
                return render(request, 'Home/menu.html')
        except:
            return render(request, 'Home/cust_Dashboard.html')
    else:
        return render(request, 'Home/index.html')


def uploadDocument(request):
    if request.user.is_authenticated:
        return render(request, 'Home//uploadDocument.html')
    else:
        return render(request, 'Home/index.html')


def uploadPicture(request):
    if request.user.is_authenticated:
        return render(request, 'Home//picUpload.html')
    else:
        return render(request, 'Home/index.html')


def custDashboard(request):
    print("hhhhhhh")
    if request.user.is_authenticated:
        return render(request, 'Home//cust_Dashboard.html')
    else:
        return render(request, 'Home/index.html')


def applyboard(request):
    if request.user.is_authenticated:
        return render(request, 'Home/applyforOnboard.html')
    else:
        return render(request, 'Home/index.html')


def menu(request):
    if request.user.is_authenticated:
        check_id = request.user.id
        try:
            if application.objects.get(appID=check_id):
                return render(request, 'Home/menu.html')
        except:
            return render(request, 'Home/cust_Dashboard.html')
    else:
        return render(request, 'Home/index.html')

def newcustmenu(request):
    if request.user.is_authenticated:
        check_id = request.user.id
        try:
            if application.objects.get(appID=check_id):
                return render(request, 'Home/menu.html')
        except:
            return render(request, 'Home/cust_Dashboard.html')
    else:
        return render(request, 'Home/index.html')



