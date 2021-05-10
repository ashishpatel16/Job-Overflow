from . import views
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('my-profile/', views.my_profile, name='my-profile'),
    path('profile/<int:user_id>/', views.view_profile, name='view-profile'),
    path('add-skill/', views.add_skill, name='add-skill'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
