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
from .views import user_love,user_order, user_cancelorder

urlpatterns = [
    url(r'^user_love/', user_love, name='user_love'),
    url(r'^user_order/(\d+)/', user_order, name='user_order'),
    url(r'^user_cancelorder/(\d+)/', user_cancelorder, name='user_cancelorder')
]
