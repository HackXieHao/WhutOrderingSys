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
from django.conf.urls import url, include, re_path
import xadmin
from users.views import index
from django.views.static import serve
from .settings import MEDIA_ROOT

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    # url分发
    url(r'^users/', include(('users.urls', 'users'), namespace='users')),
    url(r'^dishes/', include(('dishes.urls', 'dishes'), namespace='dishes')),
    url(r'^operations/', include(('operations.urls', 'operations'), namespace='operations')),
    url(r'^orderWindows/', include(('orderWindows.urls', 'orderWindows'), namespace='orderWindows')),
    url(r'^$', index, name='index'),
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
]
