from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='jobs-home'),
    path('post-job/', views.post_job, name='jobs-create'),
    path('hire/', views.hire, name='jobs-hire'),
    path('contact/', views.contact, name='jobs-contact'),
    path('about/', views.about, name='jobs-about'),

]
