from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path,include
from main.views import ProductViewSet,OrderViewSet,UserViewSet,OrderItemViewSet
router = DefaultRouter()
router.register(r'users',UserViewSet,basename='users'),
router.register(r'products',ProductViewSet,basename='product'),
router.register(r'orders',OrderViewSet,basename='order'),
router.register(r'orderitem',OrderItemViewSet,basename='orderitem')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include(router.urls))
]
