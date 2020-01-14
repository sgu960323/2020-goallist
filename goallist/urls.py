"""goallist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from Goal import views as main_views
from accounts import views as account_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.home, name="home"),
    path('main/', main_views.main, name="main"),
    path('main/detail/', main_views.post_detail, name="postdetail"),
    path('main/mypage/', main_views.mypage, name="mypage"),
    path('main/mypage/mydetail', main_views.mydetail, name="mydetail"),
    path('main/mypage/mydelete', main_views.mydelete, name="mydelete"),
    path('accounts/login/', account_views.login, name="login"),
    path('accounts/logout/', account_views.logout, name="logout"),
    path('register/', account_views.register, name="register"),
]
