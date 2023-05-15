from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect, reverse
from django.urls import reverse

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: WSGIRequest):
        unlogin_views = (reverse('login'), reverse('registration'), reverse('main'))
        if not request.user.is_authenticated and request.path not in unlogin_views:
            path = request.build_absolute_uri()
            login_url = reverse('login')
            return redirect(login_url + '?next=' + path)

        if request.user.is_authenticated and request.path in unlogin_views:
            return redirect('todo_main')

        return self.get_response(request)


