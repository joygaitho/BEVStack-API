from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status, generics

from .models import Category
from .serializers import CategorySerializer
from .permissions import IsAdminOrReadOnly

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Drink
from .serializers import DrinkSerializer

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


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class DrinkListCreateView(generics.ListCreateAPIView):
    queryset = Drink.objects.select_related("category").all()
    serializer_class = DrinkSerializer
    permission_classes = [IsAdminOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["category", "is_available"]
    search_fields = ["name", "description"]
    ordering_fields = ["price", "created_at"]


class DrinkDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drink.objects.select_related("category").all()
    serializer_class = DrinkSerializer
    permission_classes = [IsAdminOrReadOnly]
