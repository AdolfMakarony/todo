from django.urls import path
from homework.views import index, huindex


urlpatterns = [
    path('', index)
]
