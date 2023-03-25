from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerailizer,OrderSerailizer,UserSerailizer,OrderItemSerailizer
from .models import Product,Order,User,OrderItem
# from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerailizer
    queryset = Product.objects.all()
    # permission_classes = (IsAuthenticatedOrReadOnly)

    
class UserViewSet(ModelViewSet):
    serializer_class = UserSerailizer
    queryset = User.objects.all()
    # permission_classes = (IsAuthenticatedOrReadOnly)

class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerailizer
    queryset = Order.objects.all()
    # permission_classes = (IsAuthenticatedOrReadOnly)


class OrderItemViewSet(ModelViewSet):
    serializer_class = OrderItemSerailizer
    queryset = OrderItem.objects.all()
    # permission_classes = (IsAuthenticatedOrReadOnly)