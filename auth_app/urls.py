"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from auth_app.views import login_view, user_list, registration, logout_view, log_in_sys, del_usr


urlpatterns = [
    path('login/', login_view, name='login'),
    path('log_in_sys/', log_in_sys, name='log_in_sys'),
    path('del_usr/', del_usr, name='del_usr'),
    path('logout/', logout_view, name='logout'),
    path('user_list/', user_list, name='user_list'),
    path('registration/', registration, name='registration'),
]
