from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path,include
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view as drf_schema_view
from drf_yasg import openapi
from main.views import ProductViewSet,OrderViewSet,UserViewSet,OrderItemViewSet
from rest_framework.permissions import AllowAny


schema_view = drf_schema_view(
    openapi.Info(
        title="Exam Create Api",
        description="imtixon api yaratish",
        default_version='v1',
        terms_of_service="https://www.google.com/policies/terms",
        contact=openapi.Contact(email="hello@gmail.com")
    ),
    public=True,
    permission_classes=(AllowAny,)
)

router = DefaultRouter()
router.register(r'users',UserViewSet,basename='users'),
router.register(r'products',ProductViewSet,basename='product'),
router.register(r'orders',OrderViewSet,basename='order'),
router.register(r'orderitem',OrderItemViewSet,basename='orderitem')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include(router.urls)),
    path('swagger/',schema_view.with_ui("swagger",cache_timeout=0),name='swagger-docs')
]
