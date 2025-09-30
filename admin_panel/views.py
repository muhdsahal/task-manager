from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  login, logout
from django.shortcuts import render, redirect
from accounts.models import User
from tasks.models import Task
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse



def no_permission(request):
    return HttpResponse("<h2>You do not have permission to view this page.</h2>")


@login_required
def superadmin_dashboard(request):
    users = User.objects.all()
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'admin_panel/superadmin_dashboard.html', {'users': users, 'tasks': tasks})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('superadmin-dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'admin_panel/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
