from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import View

# Clase personalizada para la vista de inicio de sesión
class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('home')  # Redirige a la página de inicio después de iniciar sesión

# Clase personalizada para la vista de cierre de sesión
class CustomLogoutView(LogoutView):
    next_page = '/'  # Redirige a la página de inicio después de cerrar sesión

# Vista de inicio
class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class NotificationView(View):
    def get(self, request):
        return render(request, 'generic.html')  # Usa 'generic.html'

class RecentActivitiesView(View):
    def get(self, request):
        return render(request, 'generic.html')  # Usa 'generic.html'

class ContactsView(View):
    def get(self, request):
        return render(request, 'generic.html')  # Usa 'generic.html'

class MessagesView(View):
    def get(self, request):
        return render(request, 'generic.html')  # Usa 'generic.html'

class CalendarView(View):
    def get(self, request):
        return render(request, 'generic.html')  # Usa 'generic.html'

class SettingsView(View):
    def get(self, request):
        return render(request, 'generic.html')  # Usa 'generic.html'
