from django.urls import path
from homework.views import hw_even


urlpatterns = [
    path('hw_even_sum', hw_even)
    # path('even_sum', even)
]
