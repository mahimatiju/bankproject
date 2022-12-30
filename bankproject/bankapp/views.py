from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Detail


# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('detail')
        else:
            messages.info(request, 'Inalid credentials')
            return redirect('login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username):
                messages.info(request, 'Username already taken')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')
    return render(request, 'register.html')


def detail(request):
    if request.method == 'POST':
        name = request.POST.get('name', )
        dob = request.POST.get('dob', )
        age = request.POST.get('age', )
        gender = request.POST.get('gender', )
        phone = request.POST.get('phone', )
        email = request.POST.get('email', )
        address = request.POST.get('address', )
        district = request.POST.get('district', )
        branch = request.POST.get('branch', )
        account = request.POST.get('account', )
        material = request.POST.getlist('material', )
        detail1 = Detail(name=name, dob=dob, gender=gender, age=age, phone=phone, email=email, address=address,
                         district=district, branch=branch, account=account, material=material)
        detail1.save()
        messages.info(request, 'Application accepted!')
    return render(request, 'detail.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
