"""
URL configuration for bloggingPlatform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import home, signup
from django.contrib.auth import views as auth_views
from blog.views import home, signup, create_post, post_detail, edit_post, delete_post, add_comment, profile, delete_comment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path(
        'logout/',
        auth_views.LogoutView.as_view(next_page='home'),
        name='logout'
    ),
    path('create/', create_post, name='create_post'),
    path('post/<slug:slug>/', post_detail, name='post_detail'),
    path('post/<slug:slug>/edit/', edit_post, name='edit_post'),
    path('post/<slug:slug>/delete/', delete_post, name='delete_post'),
    path('post/<slug:slug>/comment/', add_comment, name='add_comment'),
    path('profile/', profile, name='profile'),
    path('post/<slug:slug>/comment/<int:comment_id>/delete/', delete_comment, name='delete_comment'),
]
