from django.urls import path
from . import views

urlpatterns = [
    path('user/',views.fn_reg),
    path('login/',views.fn_login),
    path('udata/',views.fn_userdata)
]