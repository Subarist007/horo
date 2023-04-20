from django.urls import path

from horoscope.views import sign_zodiac

# app_name = 'horoscope'

urlpatterns = [
    path('', sign_zodiac, name='sign_zodiac')
]
