from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import PostForm,RegisterForm,LoginForm,CommentForm
from .models import BlogPost,Comment
from datetime import date
# Create your views here.

def get_all_posts(request):
    return render(request,'index.html',{
        "all_posts": BlogPost.objects.all()

    })
def add_new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            data = BlogPost(
                title=form.cleaned_data['title'],
                subtitle=form.cleaned_data['subtitle'],
                date=date.today().strftime("%B %d, %Y"),
                body=form.cleaned_data['body'],
                author=form.cleaned_data['name'],
                img_url=form.cleaned_data['url']
            )
            data.save()
            return HttpResponseRedirect(reverse("get_all_posts"))
    else:
       form = PostForm()
    return render(request,'make-post.html', {
        'form':form,
    })

def show_post(request,post_id):
    post = BlogPost.objects.get(id=post_id)
    comment_form = CommentForm()
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            if not request.user.is_authenticated:
                messages.error(request, "You need to login or register to comment.")
                return redirect('user_login')
            new_comment = Comment(
                text=comment_form.cleaned_data["comment_text"],
                comment_author=User.username,
                parent_post=post_id
            )
            new_comment.save()
            return redirect('show_post',post_id=post_id)
    return render(request,"post.html", {
        "post":post,
        "comment_form":comment_form
    })
def edit_post(request,post_id):
    post = BlogPost.objects.get(id=post_id)
    edit_form = PostForm(initial={
        'title':post.title,
        'subtitle': post.subtitle,
        'img_url': post.img_url,
        'author': post.author,
        'body': post.body
    })
    if request.method == "POST":
        edit_form = PostForm(request.POST)
        if edit_form.is_valid():
            post.title = edit_form.cleaned_data['title']
            post.subtitle = edit_form.cleaned_data['subtitle']
            post.img_url = edit_form.cleaned_data['url']
            post.author = edit_form.cleaned_data['name']
            post.body = edit_form.cleaned_data['body']
            post.save()
            return HttpResponseRedirect(reverse("get_all_posts"))
    return render(request,"make-post.html",{
        'form':edit_form,
        'is_edit':True,
        'post':post
    })

def delete_post(request,post_id):
    post_to_delete = BlogPost.objects.get(id=post_id)
    post_to_delete.delete()
    return render(request,'index.html')

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
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            user = authenticate(request,username=name,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse("get_all_posts"))
            else:
                return render(request,"login.html",{
                    "form": form,
                    "message":"Incorrect, please try again."
                })
    else:
        form = LoginForm()
    return render(request,"login.html",{
        "form":form
    })

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("get_all_posts"))

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")