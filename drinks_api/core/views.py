from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, generics

from rest_framework import viewsets, permissions
from .models import Category, Drink
from .serializers import CategorySerializer, DrinkSerializer
from .permissions import IsAdminOrReadOnly

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    return Response(
        {
            'status': 'ok',
            'service': 'BEVStack-API'
        },
        status=status.HTTP_200_OK
    )

@csrf_exempt # Applied as requested
@api_view(['POST'])
@authentication_classes([BasicAuthentication]) # Auth config added
@permission_classes([AllowAny])
def process_webhook(request):
    """
    Example POST view with CSRF exemption and explicit Auth configuration.
    """
    if request.method == 'POST':
        # logic for processing the post data goes here
        return Response(
            {"message": "Data received successfully", "data": request.data}, 
            status=status.HTTP_201_CREATED
        )

# --- Standard Views (GET, POST, PUT, DELETE included) ---

class CategoryListCreateView(generics.ListCreateAPIView):
    # Handles: GET (list), POST (create)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    # This ONE class handles GET, PUT, PATCH, and DELETE for /categories/<id>/
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminOrReadOnly]

class DrinkListCreateView(generics.ListCreateAPIView):
    # Handles: GET (list), POST (create)
    queryset = Drink.objects.select_related("category").all()
    serializer_class = DrinkSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["category", "is_available"]
    search_fields = ["name", "description"]
    ordering_fields = ["price", "created_at"]


class DrinkDetailView(generics.RetrieveUpdateDestroyAPIView):
    # Handles: GET (retrieve), PUT/PATCH (update), DELETE (destroy_
    queryset = Drink.objects.select_related("category").all()
    serializer_class = DrinkSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminOrReadOnly]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('-created_at')
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class DrinkViewSet(viewsets.ModelViewSet):
    queryset = Drink.objects.select_related('category').all().order_by('-created_at')
    serializer_class = DrinkSerializer
    permission_classes = [permissions.IsAuthenticated]
