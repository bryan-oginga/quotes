from django.urls import path
from .views import random_quotes

app_name = 'homepage'

urlpatterns = [
    path('',random_quotes,name='home'),
   
]