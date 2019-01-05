from django.http import HttpResponseRedirect
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from main.models import Post
from django import forms
from django.urls import reverse
from .forms import AllForm
from django.contrib import auth
from django.contrib.auth import authenticate, login,logout
import datetime,re


def auth(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/main/1')
    else:
        authform = {'authform': AllForm(), 'login': request.user}
        return render(request, 'auth.html',authform)

def check(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/auth/')
    else:
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/main/1')
            else:
                return HttpResponseRedirect('/auth/')
        else:
            return HttpResponseRedirect('/auth/')

def view(request,page):

    if not request.user.is_authenticated:
        return HttpResponseRedirect('/auth/')
    else:
        posts_on_page = 10
        posts = Post.objects.order_by('-id')

        if posts.count() % posts_on_page == 0:
            buttons = (posts.count() // posts_on_page)
        else:
            buttons = (posts.count() // posts_on_page) + 1

        posts = Post.objects.order_by('-id')[(page -1)*posts_on_page: page*posts_on_page]

        count = {x+1: (x+1) for x in range(buttons)}
        post = {'post': posts, 'form': AllForm(),'count': count,'login': request.user}

        cookie(request)

        return render(request,'main.html',post)


def newdata(request):

    if request.method == 'POST':
        form = AllForm(request.POST)
        if form.is_valid():
            info = Post(name=form.data.get('name'),
                        surname=form.data.get('surname'),
                        fathername=form.data.get('fathername'),
                        phone=form.data.get('phone'),
                        description=form.data.get('description'),
                        date=datetime.datetime.now())
            info.save()
    return HttpResponseRedirect('/main/1')

def find(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/auth/')
    else:
        find = AllForm(request.POST).data.get('find')
        posts = Post.objects.filter(surname=find).order_by('-id')
        post = {'post': posts, 'form': AllForm()}
        return render(request, 'main.html', post)


#-------------------------------------------------------------------------------------

def cookie(request):
    if request.COOKIES:
        for key in request.COOKIES:
            if key == 'csrftoken':
                pass

            else:
                a = 0
                while key[a].isdecimal(): a += 1

                if key[a:] == 'name':
                    Post.objects.filter(id=key[0:a]).update(name=request.COOKIES.get(key))
                elif key[a:] == 'surname':
                    Post.objects.filter(id=key[0:a]).update(surname=request.COOKIES.get(key))
                elif key[a:] == 'fathername':
                    Post.objects.filter(id=key[0:a]).update(fathername=request.COOKIES.get(key))
                elif key[a:] == 'phone':
                    if re.match(r'^8-\d{3}-\d{3}-\d{2}-\d{2}$',request.COOKIES.get(key)):
                        Post.objects.filter(id=key[0:a]).update(phone=request.COOKIES.get(key))
                elif key[a:] == 'delete':
                    Post.objects.filter(id=key[0:a]).delete()
    #        request.COOKIES.delete_cookie

    else:
        pass

# Create your views here.
