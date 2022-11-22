from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render,redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        Password=request.POST['Password']
        user=auth.authenticate(username=username, Password=Password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid nayantharaapp")
            return redirect('nayantharaapp:login')

    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        Email = request.POST['Email']
        Password = request.POST['Password']
        cpassword = request.POST['Password1']

        if Password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username Taken")
                return redirect('register')
            elif User.objects.filter(email=Email).exists():
                messages.info(request, "email Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, Password=Password, first_name=first_name,last_name=last_name)
                user.save();
                return redirect('login')
        else:
            messages.info(request, "Password not matching")
            return redirect('register')
            return redirect('/')

    return render(request, "register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')