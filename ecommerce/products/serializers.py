from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "title", "description", "price", "image", "slug", "added_by", "category")
        read_only_fields = ("slug", "added_by")
    
    def create(self, validated_data):
        validated_data['added_by'] = self.context['request'].user

        return super(ProductSerializer, self).create(validated_data)

class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "title", "description", "price", "image", "slug","category", "added_by")
        read_only_fields = ("slug", "added_by")
    
    def create(self, validated_data):
        validated_data['added_by'] = self.context['request'].user
        return super(CreateProductSerializer, self).create(validated_data)

class UpdateProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)  # Set required=False for the 'image' field

    class Meta:
        model = Product
        fields = ("id", "title", "description", "price", "slug", "image", "added_by")
        read_only_fields = ("slug", "added_by")
    
    def update(self, instance, validated_data):
        return super(UpdateProductSerializer, self).update(instance, validated_data)
