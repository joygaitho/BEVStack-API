from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, DrinkViewSet
from .views import RegisterView
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'drinks', DrinkViewSet)
urlpatterns = router.urls


from django.urls import path
from .views import (
    health_check,
    CategoryListCreateView,
    CategoryDetailView,
    DrinkListCreateView,
    DrinkDetailView,
    process_webhook,
) 

urlpatterns = [
    path('health/', health_check, name='health_check'),
    path('webhook/', process_webhook, name='process-webhook'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('drinks/', DrinkListCreateView.as_view(), name='drink-list-create'),
    path('drinks/<int:pk>/', DrinkDetailView.as_view(), name='drink-detail'),
    path('register/', RegisterView.as_view(), name='register'),

] + router.urls