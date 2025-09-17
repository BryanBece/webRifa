# rifa/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('ticket/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
    path('add_ticket/<int:numero>/', views.add_ticket, name='add_ticket'),
    path('update-ticket/<int:ticket_id>/', views.update_ticket, name='update_ticket'),
    path('delete-ticket/<int:ticket_id>/', views.delete_ticket, name='delete_ticket'),
    path('login/', LoginView.as_view(template_name='rifa/registration/login.html', redirect_authenticated_user=True), name='login'),
    path('profile/', views.profile, name='profile'),
    path('tickets/pdf/', views.tickets_pdf, name='tickets_pdf'),
    path('logout/', logout, name='logout'),
]
