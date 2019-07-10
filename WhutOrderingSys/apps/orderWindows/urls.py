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
from .views import window_list, window_detail, window_detail_dishes, window_detail_intro

urlpatterns = [
   url(r'^window_list', window_list, name='window_list'),
   url(r'^window_detail/(\d+)/', window_detail, name='window_detail'),
   url(r'^window_detail_dishes/(\d+)/', window_detail_dishes, name='window_detail_dishes'),
   url(r'^window_detail_intro/(\d+)/', window_detail_intro, name='window_detail_intro')
]
