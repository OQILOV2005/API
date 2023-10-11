from django.urls import path
from . import views


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
