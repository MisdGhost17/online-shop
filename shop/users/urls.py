from django.urls import path
from users.views import login, logout, registration, update


urlpatterns = [
    path('account/login', login, name='loginform'),
    path('account/logout', logout, name='logoutform'),
    path('account/registration', registration, name='registrationform'),
    path('account/profileupdate', update, name='profileupdateform'),


]