from . import views
from django.urls import path, include
from .views import JobListView, JobCreateView, JobUpdateView, JobDeleteView, JobDetailView

urlpatterns = [
    path('', JobListView.as_view(), name='jobs-home'),
    path('jobs/new/', JobCreateView.as_view(), name='jobs-create'),
    path('jobs/<int:pk>/', JobDetailView.as_view(), name='jobs-detail'),
    path('jobs/<int:pk>/update', JobUpdateView.as_view(), name='jobs-update'),
    path('jobs/<int:pk>/delete', JobDeleteView.as_view(), name='jobs-delete'),
    path('hire/', views.hire, name='jobs-hire'),
    path('contact/', views.contact, name='jobs-contact'),
    path('about/', views.about, name='jobs-about'),
    path('testimonials/',views.testimonials,name='testimonials')
]
