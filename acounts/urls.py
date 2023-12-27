from django.urls import path
from .views import signup, activate

app_name = 'acounts'

urlpatterns = [
    path('signup/', signup , name='signup'),
    path('<str:username>/activate', activate, name='activate'),
]


