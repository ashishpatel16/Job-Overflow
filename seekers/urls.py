from . import views
from django.urls import path, include


urlpatterns = [
    path('my-profile/', views.my_profile, name='my-profile'),
    path('profile/<int:user_id>/', views.view_profile, name='view-profile'),
    path('add-skill/', views.add_skill, name='add-skill'),
    
]
