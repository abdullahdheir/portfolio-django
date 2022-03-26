import re
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages,auth
from .models import MyData
from django.contrib.auth import authenticate

# Create your views here.

def index(requset):
    myData = MyData.objects.get()
    return render(requset,'index.html',{'myDatas':myData})

def blog(requset):
    d = []
    for i in range(100):
        d.append(i)
    return render(requset,'blog.html',{'data':d})

def portfolioDetails(requset):
    myData = MyData.objects.get()
    return render(requset,'portfolio-details.html',{'myDatas':myData})

def innerPage(requset):
    myData = MyData.objects.get()
    return render(requset,'inner-page.html',{'myDatas':myData})

def validateEmail(email):
    if len(email) > 6:
        if re.match('\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b', email) != None:
            return 1
    return 0

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            mail = request.POST['email']
            password = request.POST['password']
            conPass = request.POST['password2']

            if len(username) < 4 or username == '' :
                messages.info(request,'Invaild Username')
                return redirect('register')
            elif mail == '':
                messages.info(request,'Invaild Email')
                return redirect('register')
            elif password == '':
                messages.info(request,'Con\'t Be Password Feild Empty !!')
                return redirect('register')

            if password == conPass :
                if User.objects.filter(email = mail).exists():
                    messages.info(request,'The Email Already Used')
                    return redirect('register')
                elif User.objects.filter(username = username).exists():
                    messages.info(request,'Username Unavailable')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username = username,email = mail,password = password)
                    user.save()
                    return redirect('login')
            else:
                messages.info(request,'Password Not Match')
                return redirect('register')
        else:
            return render(request,'register.html')

def login(request):
    if request.user.is_authenticated :
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request,username = username,password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.info(request,'Invaild UserName or Password ,Please Try Again')
                return redirect('login')
        else:
            return render(request,'login.html')

def error_404_view(request, exception):
    return render(request,'error_404.html')

def logout(request):
    auth.logout(request)
    return redirect('login')
    