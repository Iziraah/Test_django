from django.views.generic import ListView
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import  ProductSerializer, UserSerializer, LessonSerializer
from .models import Product, User
from django.shortcuts import get_object_or_404, render

def my_view(request):
    context = {"name": "John"}
    return render(request, "myapp/my_template.html", context)


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.prefetch_related('lesson_set').all()

def user_lessons(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    lessons = user.lessons_accessed.all()

    return render(request, 'myapp/user_lessons.html', {'user': user, 'lessons': lessons})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'])
    def user_lessons(self, request, pk=None):
        user = self.get_object()
        lessons = user.lessons_accessed.all()
        serializer = LessonSerializer(lessons, many=True) 
        return Response(serializer.data)
    
class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Product.objects.prefetch_related('lesson_set').all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        lessons = product.lesson_set.all()
        users = User.objects.filter(lessons_accessed__in=lessons).distinct()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)