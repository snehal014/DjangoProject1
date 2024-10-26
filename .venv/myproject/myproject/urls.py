"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from firstapp import views

urlpatterns = [
    path('', views.client_list, name='client_list'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('client/<int:client_id>/', views.client_detail, name='client_detail'),
    path('add-client/', views.register_client, name='register_client'),
    path('edit-client/<int:id>/', views.edit_client, name='edit_client'),
    path('delete-client/<int:id>/', views.delete_client, name='delete_client'),
    path('add-project/<int:client_id>/', views.add_project, name='add_project'),
    path('assign-project/<int:project_id>/', views.assign_project, name='assign_project'),
    path('assigned-projects/', views.assigned_projects, name='assigned_projects'),
    path('client-projects/<int:client_id>/', views.client_projects, name='client_projects'),
]

