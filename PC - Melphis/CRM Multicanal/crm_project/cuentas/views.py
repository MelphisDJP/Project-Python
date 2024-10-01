from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.shortcuts import render

class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('home')  # Redirige a la página de inicio después de iniciar sesión

class CustomLogoutView(LogoutView):
    next_page = '/'  # Redirige a la página de inicio después de cerrar sesión

def home(request):
    return render(request, 'home.html')

def notification_view(request):
    return render(request, 'notification.html')  # Asegúrate de que tengas una plantilla para esto

def recent_activities_view(request):
    return render(request, 'recent_activities.html')  # Asegúrate de que tengas una plantilla para esto

def contacts_view(request):
    return render(request, 'contacts.html')