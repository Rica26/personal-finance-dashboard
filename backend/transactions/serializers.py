from rest_framework import serializers
from .models import Transaction, Category


class TransactionSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    class Meta:
        model = Transaction
        fields = ['id', 'category', 'category_name', 'amount', 'date', 'created_at', 'updated_at']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'type']

    def validate(self, data):
        qs = Category.objects.filter(name=data['name'], type=data['type'])
        if self.instance:
            qs = qs.exclude(id=self.instance.id)
        if qs.exists():
            raise serializers.ValidationError("Category with this name and type already exists.")
        return data
    
    def validate_name(self, value):
        if not value:
            return value
        cat_type = self.initial_data.get('type')
        if cat_type and value not in Category.NAME_CHOICES.get(cat_type, []):
            raise serializers.ValidationError(f"Invalid category name '{value}' for type '{cat_type}'. Allowed names are: {Category.NAME_CHOICES.get(cat_type, [])}")
        return value