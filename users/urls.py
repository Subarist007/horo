from django.urls import path

from users.views import login, registration

# app_name = 'login'

urlpatterns = [
    path('', login, name='login'),
    path('registration/', registration, name='registration'),
]