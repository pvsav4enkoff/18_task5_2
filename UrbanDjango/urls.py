"""
URL configuration for UrbanDjango1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from task2.views import task2_func_view, ViewByClass, task2_func_view2
from task3.views import task3_view_platform, task3_view_games, task3_view_cart
from task4.views import task4_view_platform, task4_view_games, task4_view_cart
from task5.views import sign_up_by_html, sign_up_by_django
urlpatterns = [
    path('',sign_up_by_html),
    path('django_sign_up/',sign_up_by_django),
    path('platform/',task4_view_platform),
    path('platform/games/',task4_view_games),
    path('platform/cart/',task4_view_cart),
    # path('', task2_func_view2),
    path('admin/', admin.site.urls),
    path('func_view/', task2_func_view),
    path('class_view/', ViewByClass.as_view())
]
