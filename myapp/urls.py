from django.urls import include, path
from .views import  ProductViewSet, my_view,  user_lessons
from rest_framework.routers import DefaultRouter
from .views import UserViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('', my_view, name='index'),
    path('user_lessons/<int:user_id>/', user_lessons, name='user-lessons'),
    path('api/', include(router.urls)),
    path('api/products/', ProductViewSet.as_view({'get': 'list'}), name='product-list'),
    path('api/products/<int:pk>/lessons_users/', ProductViewSet.as_view({'get': 'retrieve'}), name='product-lessons-users'),
]