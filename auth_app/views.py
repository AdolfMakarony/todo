from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.handlers.wsgi import WSGIRequest
from django.core.validators import validate_email
from django.shortcuts import render, redirect


# Create your views here.
def login_view(request: WSGIRequest):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        next_page = request.GET.get('next')

        user: User = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is None:
            return render(request, 'login.html', {
                'error_message': 'Неправельный логин или пароль',
            })
        login(request, user)

        if next_page is not None:
            return redirect(next_page)

        return render(request, 'info.html', {
            'content' : 'Login successful',
        })
    return render(request, 'login.html')


def registration(request: WSGIRequest):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        email = request.POST['email']

        if User.objects.filter(username=username).exists():
            return render(request, 'registration.html', {
                'error_message': 'User is already exists'
            })

        if password != password_confirm:
            return render(request, 'registration.html', {
                'error_message': 'Passes not mach'
            })

        if len(password) < 10:
            return render(request, 'registration.html', {
                'error_message': 'Short PASS'
            })

        if User.objects.filter(email=email).exists():
            return render(request, 'registration.html', {
                'error_message': 'Email is already exists'
            })

        try:
            validate_email(email)
        except ValidationError:
            return render(request, 'registration.html', {
                'error_message': 'Email is incorrect'
            })

        user = User()
        user.username = username
        user.set_password(password)
        user.email = email

        try:
            user.save()
            login(request, user)
        except Exception as e:
            return render(request, 'registration.html', {
                'error_message': 'Server error'
            })

        return render(request, 'info.html', {
            'content': 'Success'
        })

    return render(request, 'registration.html')


def user_list(request: WSGIRequest):
    if not request.user.is_superuser:
        return render(request, 'info.html', {
            'content': 'Not allowed'
        })
    users = User.objects.all()
    return render(request, 'user_list.html', {
        'users' : users
    })

def logout_view(request: WSGIRequest):
    logout(request)
    return redirect('login')

def log_in_sys(request: WSGIRequest):
    user = User.objects.get(pk=request.POST["user_id"])
    login(request, user)
    return redirect('login')

def del_usr(request: WSGIRequest):
    user = User.objects.get(pk=request.POST["user_id"])
    if not user.is_superuser:
        user.delete()
        return redirect('user_list')
    else:
        return render(request, 'info.html', {
            'content': 'Sosi jopu'
        })