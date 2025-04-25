from django.urls import path
from users.views import login, logout, registration, update


urlpatterns = [
    path('account/login', login, name='login'),
    path('account/logout', logout, name='logout'),
    path('account/registration', registration, name='registration'),
    path('account/profileupdate', update, name='profileupdate'),
]