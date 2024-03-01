from rest_framework import serializers
from .models import Product, User, Lesson

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    lessons_accessed = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'