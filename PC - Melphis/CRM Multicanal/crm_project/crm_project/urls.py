# crm_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cuentas.urls')),  # Incluye las URLs de la app cuentas para la raíz
]