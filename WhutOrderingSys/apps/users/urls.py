"""WhutOrderingSys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
from .views import user_login, user_logout, user_register, user_center, usermanage_changeimage, usermanage_changeinfo,user_changepwd,user_orderInfo, user_lovedish, user_lovewindow, user_submitorder, user_cancelorder

urlpatterns = [
    url(r'user_login', user_login, name='user_login'),
    url(r'user_logout', user_logout, name='user_logout'),
    url(r'user_register', user_register, name='user_register'),
    url(r'user_center/', user_center, name='user_center'),
    url(r'usermanage_changeimage', usermanage_changeimage, name='usermanage_changeimage'),
    # 修改用户信息
    url(r'usermanage_changeinfo', usermanage_changeinfo, name='usermanage_changeinfo'),
    # 在个人中心修改密码
    url(r'user_changepwd', user_changepwd, name='user_changepwd'),
    url(r'user_orderInfo', user_orderInfo, name='user_orderInfo'),
    url(r'user_lovedish', user_lovedish, name='user_lovedish'),
    url(r'user_lovewindow', user_lovewindow, name='user_lovewindow'),

    url(r'user_submitorder', user_submitorder, name='user_submitorder'),
    url(r'user_cancelorder', user_cancelorder, name='user_cancelorder')
]
