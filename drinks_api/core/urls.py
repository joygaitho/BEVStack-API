from django.urls import path
from .views import (
    health_check,
    CategoryListCreateView,
    CategoryDetailView,
    DrinkListCreateView,
    DrinkDetailView,
) 

urlpatterns = [
    path('health/', health_check, name='health_check'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('drinks/', DrinkListCreateView.as_view(), name='drink-list-create'),
    path('drinks/<int:pk>/', DrinkDetailView.as_view(), name='drink-detail'),

]