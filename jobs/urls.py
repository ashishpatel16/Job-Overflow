from . import views
from seekers import views as seeker_views
from django.urls import path, include
from .views import JobListView, JobCreateView, JobUpdateView, JobDeleteView, JobDetailView, JobApplicationDetailView

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', JobListView.as_view(), name='jobs-home'),
    path('jobs/new/', JobCreateView.as_view(), name='jobs-create'),
    path('jobs/<int:pk>/', JobDetailView.as_view(), name='jobs-detail'),
    path('jobs/<int:pk>/update', JobUpdateView.as_view(), name='jobs-update'),
    path('jobs/<int:pk>/delete', JobDeleteView.as_view(), name='jobs-delete'),
    path('hire/', views.hire, name='jobs-hire'),
    path('contact/', views.contact, name='jobs-contact'),
    path('about/', views.about, name='jobs-about'),
    path('apply/<int:job_id>', views.apply, name='apply'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('search/', views.search, name='search'),
    path('jobs/applications/<int:pk>/',
         JobApplicationDetailView.as_view(), name='jobapplication-detail'),
    path('jobs/application/<int:pk>/',
         views.view_applications, name='view-application'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
