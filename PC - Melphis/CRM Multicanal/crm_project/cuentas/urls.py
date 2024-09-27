# cuentas/urls.py
from django.urls import path, re_path
from django.views.generic.base import RedirectView
from .views import CustomLoginView, CustomLogoutView, home

urlpatterns = [
    re_path(r'^$', RedirectView.as_view(url='/login/', permanent=False), name='login_redirect'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('home/', home, name='home'),
]
