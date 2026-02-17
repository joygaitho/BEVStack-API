from rest_framework import serializers
from .models import Category, Drink


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at']
        read_only_fields = ['id', 'created_at']

class DrinkSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value

    class Meta:
        model = Drink
        fields = [
            'id',
            'name',
            'description',
            'price',
            'category',
            'image_url',
            'category_name',
            'is_available',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'category_name']
