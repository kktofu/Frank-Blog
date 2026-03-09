from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponseForbidden
from django.urls import reverse
from .forms import PostForm,RegisterForm,LoginForm,CommentForm
from .models import BlogPost,Comment
from datetime import date
# Create your views here.

def get_all_posts(request):
    return render(request,'index.html')

def add_new_post(request):
    form = PostForm()

    return render(request, 'make-post.html', {
        "form": form,
        "is_edit": False
    })

def show_post(request, post_id):
    comment_form = CommentForm()
    return render(request, "post.html", {
        "post_id": post_id,
        "comment_form": comment_form
    })

def edit_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)

    edit_form = PostForm(initial={
        'title': post.title,
        'subtitle': post.subtitle,
        'img_url': post.img_url,
        'body': post.body
    })

    return render(request, "make-post.html", {
        'form': edit_form,
        'is_edit': True,
        'post': post
    })



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            user.save()
            return HttpResponseRedirect(reverse("get_all_posts"))
    else:
        form = RegisterForm()
    return render(request,"register.html",{
        "form":form
    })

def user_login(request):
    form = LoginForm()
    return render(request,"login.html",{
        "form":form
    })


def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")