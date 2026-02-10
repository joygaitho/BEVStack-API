from django.urls import path
from .views import (
    health_check,
    CategoryListCreateView,
    CategoryDetailView,
) 

urlpatterns = [
    path('health/', health_check, name='health_check'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
]