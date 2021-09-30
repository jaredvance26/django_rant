from django.urls import path
from .views import (PostView, PostDetailView, PostCreateView)
from . import views

urlpatterns = [
    path('', PostView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='blog-about'),
]
