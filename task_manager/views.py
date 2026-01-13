from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib import messages

def index_view(request):
    return render(request, 'task_manager/index.html')

# Временные представления для заглушек
def users_index(request):
    return HttpResponse("<h1>Users page (temporary)</h1><p>This will be implemented later.</p>")

def statuses_index(request):
    return HttpResponse("<h1>Statuses page (temporary)</h1><p>This will be implemented later.</p>")

def labels_index(request):
    return HttpResponse("<h1>Labels page (temporary)</h1><p>This will be implemented later.</p>")

def tasks_index(request):
    return HttpResponse("<h1>Tasks page (temporary)</h1><p>This will be implemented later.</p>")

def users_create(request):
    return HttpResponse("<h1>Registration page (temporary)</h1><p>This will be implemented later.</p>")

def login_view(request):
    # Просто редирект на главную страницу
    messages.info(request, "Login functionality will be implemented later.")
    return redirect('index')

def logout_view(request):
    # Просто редирект на главную страницу
    messages.info(request, "Logout functionality will be implemented later.")
    return redirect('index')
