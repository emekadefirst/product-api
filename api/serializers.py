from rest_framework import serializers
from .models import Brand, Category, Product

class BaseSerializer(serializers.ModelSerializer):
    """Reusable base serializer with generic create and update methods."""

    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

class BrandSerializer(BaseSerializer):
    class Meta:
        model = Brand
        fields = ["id", "name", "image"]
        extra_kwargs = {"id": {"read_only": True}}

class CategorySerializer(BaseSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]
        extra_kwargs = {"id": {"read_only": True}}

class ProductSerializer(BaseSerializer):
    brand = serializers.SlugRelatedField(slug_field="name", queryset=Brand.objects.all())
    category = serializers.SlugRelatedField(slug_field="name", queryset=Category.objects.all())
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "brand",
            "category",
            "image",
            "description",
            "price",
            "quantity",
            "created_at",
        ]
        extra_kwargs = {"id": {"read_only": True}, "created_at": {"read_only": True}}
