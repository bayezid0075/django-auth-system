from django.urls import path
from . import views
urlpatterns = [
    path('',  views.home),
    path('signup/',  views.user_signup, name='signup'),
    path('login/',  views.login, name='login'),
    path('logout/',  views.logout, name='logout')
]