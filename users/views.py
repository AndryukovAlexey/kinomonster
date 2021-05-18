from django.shortcuts import render, redirect
from .forms import Registr, Confirm, SupportForm, UpdateProfile, ProfileAvatar #UpdatePassword
from django.contrib import messages
from movies.views import news, rat_movie
from movies.models import Likes
from users.models import Premka
import random
from django.core.mail import send_mail
from kinomonster import settings
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeForm
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import datetime


def regCode():
    code = random.randint(10000, 99999)
    return str(code)

def registr(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    else:
        error = None
        if request.method == 'POST':
            form = Registr(request.POST)

            if form.is_valid():
                email = form.cleaned_data.get('email')

                if not User.objects.filter(email=email):

                    user = form.save(commit=False)          
                    user.is_active = False
                    user.save()      
                    request.session['id'] = user.id
                    subject = 'Код подтверждения'
                    code = regCode()
                    message = code

                    request.session['code'] = message
                    from_email = 'lehaandrukov117@gmail.com'
                    

                    mail = send_mail(subject, message, from_email, [email], fail_silently=False)

                    if mail:
                        messages.success(request, 'Письмо с кодом отправлено')
                        return redirect('conf-page')
                        if conf():
                            return redirect('reg-page')
                    else:
                        messages.error(request, 'Ошибка отправки')
                else:
                    error = 'Пользователь с такой почтой уже существует'
                
                        
        else:
            form = Registr()

        return render(request, 'users/registr.html', {'form': form, 'title': 'Регистрация', 'news': news, 'error': error, 'rat_movie': rat_movie})


def cont(request):
    return render(request, 'users/cont.html', {'title': 'support', 'news': news, 'rat_movie': rat_movie})


def conf(request):

    if request.method == 'POST':

        form = Confirm(request.POST)

        if form.is_valid():
            code = request.session['code']
            code_user = form.cleaned_data.get('cnf')
            session_id = request.session['id']
            if str(code_user) == code:
                user = User.objects.get(id=session_id)
                user.is_active = True
                user.save()
                messages.success(request, 'Вы зареганы!')
                return redirect('login-page')
            else:
                messages.error(request, 'Коды не совпадают!')
        

    else:
        form = Confirm()
    return render(request, 'users/conf.html', {'form': form, 'title': 'Подтверждение почты', 'news': news, 'rat_movie': rat_movie})


class Log(LoginView):
    
    def get_context_data(self, **kwargs):
        ctx = super(Log, self).get_context_data(**kwargs)
        ctx['title'] = 'auth'
        ctx['news'] = news
        ctx['rat_movie'] = rat_movie
        return ctx


def support_user(request):

    if request.method == 'POST':  
        form = SupportForm(request.POST)

        if form.is_valid():
            user = User.objects.get(username=request.user)
            email_user = user.email          
  
            subject = form.cleaned_data.get('theme')

            message = form.cleaned_data.get('text') + f'\n\n\nот {email_user}'

            from_email = email_user
            
            
            mail = send_mail(subject, message, from_email, ['helpkinomonster@gmail.com'], fail_silently=False)

            if mail:
                messages.success(request, 'Письмо отправлено')
            else:
                messages.error(request, 'Ошибка отправки')
            
        
    else:
        form = SupportForm()
                        
    return render(request, 'users/cont.html', {'form': form, 'title': 'support', 'news': news, 'rat_movie': rat_movie})



class UserDetailView(DetailView):
    
    model = User
    context_object_name = 'userik'
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = "users/profile.html"

    def get_context_data(self, **kwargs):
        ctx = super(UserDetailView, self).get_context_data(**kwargs)
        ctx['like'] = Likes.objects.all()
        ctx['news'] = news
        ctx['abiba'] = Group.objects.get(name="abiba")
        ctx['rat_movie'] = rat_movie
        return ctx

@login_required
def update_profile(request):
    if request.method == 'POST':  
        avatar_form = ProfileAvatar(request.POST, request.FILES, instance=request.user.profile)
        update_form = UpdateProfile(request.POST, instance=request.user)
        if update_form.is_valid() and avatar_form.is_valid():
            
            # print(transliterate.translit(str(avatar_form.cleaned_data.get('avatar')), reversed=True))

            # user = avatar_form.save(commit=False)          
            # avatar = avatar_form.cleaned_data.get('avatar')
            # print(avatar)
            # print(avatar.decode('ascii'))
            # user.avatar = avatar.decode('ascii')
            # user.save()
            
            avatar_form.save()
            update_form.save()
            messages.success(request, 'Данные обновлены')

            return HttpResponseRedirect(request.META['HTTP_REFERER'])
            
        
    else:
        avatar_form = ProfileAvatar(instance=request.user.profile)
        update_form = UpdateProfile(instance=request.user)
        

    return render(request, 'users/update.html', {'avatar_form': avatar_form, 'update_form': update_form, 'title': 'update profile', 'news': news, 'rat_movie': rat_movie})



@login_required
def update_password(request):
    
    if request.method == 'POST':  
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Пароль обновлен')

            # return HttpResponseRedirect(request.META['HTTP_REFERER']) 
            ret = str(request.user)
            return redirect('/' + ret + '/')
            
        
    else:
        form = PasswordChangeForm(request.user)
        
    
    return render(request, 'users/update-password.html', {'form': form, 'title': 'update password', 'news': news, 'rat_movie': rat_movie})

import hashlib

from django.views.decorators.csrf import csrf_exempt
from movies.models import News

@csrf_exempt 
def check_order(request):
	if request.method == 'POST':
		notification_type = request.POST.get('notification_type')
		operation_id = request.POST.get('operation_id')
		amount = request.POST.get('amount')
		currency = request.POST.get('currency')
		datetime = request.POST.get('datetime')
		sender = request.POST.get('sender')
		codepro = request.POST.get('codepro')
		notification_secret = 'otdjWvb5L/ny+m9CdBuwLrKV'
		label = request.POST.get('label')
		sha1_hash = request.POST.get('sha1_hash')

		sha1 = f'{notification_type}&{operation_id}&{amount}&{currency}&{datetime}&{sender}&{codepro}&{notification_secret}&{label}'
		hash_object = hashlib.sha1(bytes(sha1, encoding = 'utf-8'))
		hex_dig = hash_object.hexdigest()

		if hex_dig == str(sha1_hash):
			user = User.objects.filter(username='owner')[0]
			# News.objects.create(text=user)
			Premka.objects.create(user=user)
			Group.objects.get(name='abiba').user_set.add(user)
        
	return HttpResponse("200 OK")

def order_success(request):
    messages.success(request, 'Спасибо за покупку, наслаждайтесь фильмами!!')
    return redirect('/')
