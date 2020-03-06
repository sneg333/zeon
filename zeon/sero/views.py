from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *


def sero(request):

    if request.method == 'POST':
        user_name = request.POST[' user_name']
        user_mail = request.POST['user_mail']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if Muser.objects.filter(user_name=user_name).exists():
                messages.info(request, 'user name taken')
                return redirect('sero')
            elif Muser.objects.filter(user_mail=user_mail).exists():
                messages.info(request, 'user_mail taken')
                return redirect('sero')
            else:
                user = Muser.objects.create_user(user_name=user_name, password=password1, user_mail=user_mail)
                user.save();
                print('user created')

        else:
            messages.info(request, 'password not match')
            return redirect('register')
        return redirect('/')

    else:
        return render(request, 'sero.html')