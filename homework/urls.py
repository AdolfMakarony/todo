from django.urls import path
from homework.views import hw_even, hw_sentence_case, hw_lower_case, hw_upper_case, hw_cap_word_case, hw_toggle_case


urlpatterns = [
    path('hw_even_sum', hw_even),
    path('change_case/sentence_case', hw_sentence_case),
    path('change_case/lower_case', hw_lower_case),
    path('change_case/upper_case', hw_upper_case),
    path('change_case/capitalize_each_word', hw_cap_word_case),
    path('change_case/toggle_case', hw_toggle_case),
]
