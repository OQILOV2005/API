"""
URL configuration for setting project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from  .import views


urlpatterns = [
    path("get-banner/", views.get_banner_view),
    path("get-teams/", views.get_teams_views),
    path('get-contact/', views.create_contact_views),
    path('get-about/', views.get_about_views),
    path('get-images/', views.get_image_views),
    path('get-skill/', views.get_skill_views),
    path('get-service/', views.get_service_views),
    path('get-testimonial/', views.get_testimonial_views)
    ]
