"""
URL configuration for task_manager project.

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
from django.urls import path, include
from . import views


# Временные URL-паттерны для каждого "приложения"
users_patterns = [
    path('', views.users_index, name='index'),
    path('create/', views.users_create, name='create'),
]

statuses_patterns = [
    path('', views.statuses_index, name='index'),
]

labels_patterns = [
    path('', views.labels_index, name='index'),
]

tasks_patterns = [
    path('', views.tasks_index, name='index'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', views.index_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('users/', include((users_patterns, 'users'))),
    path('statuses/', include((statuses_patterns, 'statuses'))),
    path('labels/', include((labels_patterns, 'labels'))),
    path('tasks/', include((tasks_patterns, 'tasks'))),
]
