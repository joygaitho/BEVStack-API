from rest_framework import serializers
from ..models import Drink


class DrinkSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source="category.name")

    class Meta:
        model = Drink
        fields = [
            "id",
            "name",
            "description",
            "price",
            "is_available",
            "image_url",
            "category",
            "category_name",
            "created_at",
        ]
        read_only_fields = ["id", "created_at", "category_name"]
