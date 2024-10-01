from django.urls import path, re_path
from django.views.generic.base import RedirectView
from .views import (
    CustomLoginView,
    CustomLogoutView,
    HomeView,
    NotificationView,
    RecentActivitiesView,
    ContactsView,
    MessagesView,
    CalendarView,
    SettingsView,
)

urlpatterns = [
    re_path(r'^$', RedirectView.as_view(url='/login/', permanent=False), name='login_redirect'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('home/', HomeView.as_view(), name='home'),
    path('notification/', NotificationView.as_view(), name='notification'),
    path('recent_activities/', RecentActivitiesView.as_view(), name='recent_activities'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('messages/', MessagesView.as_view(), name='messages'),
    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('settings/', SettingsView.as_view(), name='settings'),
]
