from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages

def home(request):
    query = request.GET.get('q')
    post_list = Post.objects.all().order_by('-created_at')

    if query:
        post_list = post_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )

    paginator = Paginator(post_list, 5)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, "blog/home.html", {"posts": posts})

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect("signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("signup")

        user = User.objects.create_user(
            username=username,
            password=password1
        )

        login(request, user)
        return redirect("home")

    return render(request, "blog/signup.html")


@login_required
def create_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        Post.objects.create(
            title=title,
            content=content,
            author=request.user
        )
        return redirect("home")

    return render(request, "blog/create_post.html")

# def post_detail(request, pk):
#     # post = Post.objects.get(id=pk)
#     post = get_object_or_404(Post, slug=slug)
#     return render(request, "blog/post_detail.html", {"post": post})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post_detail.html", {"post": post})

@login_required
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to edit this post.")

    if request.method == "POST":
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        post.save()
        return redirect("post_detail", slug=post.slug)

    return render(request, "blog/edit_post.html", {"post": post})

@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this post.")

    post.delete()
    return redirect("home")

@login_required
def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        content = request.POST.get("content")

        Comment.objects.create(
            post=post,
            author=request.user,
            content=content
        )

    return redirect("post_detail", slug=slug)
    
@login_required
def profile(request):
    user_posts = Post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, "blog/profile.html", {"posts": user_posts})

@login_required
def delete_comment(request, slug, comment_id):
    post = get_object_or_404(Post, slug=slug)
    comment = get_object_or_404(Comment, id=comment_id, post=post)

    if comment.author != request.user:
        return HttpResponseForbidden("You cannot delete this comment.")

    comment.delete()
    return redirect("post_detail", slug=slug)