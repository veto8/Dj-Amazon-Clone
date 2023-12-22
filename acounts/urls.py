from django.urls import path
from .views import signup

app_name = 'acounts'

urlpatterns = [
    path('signup/',signup)
]


