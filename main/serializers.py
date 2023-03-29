from rest_framework import serializers
from .models import Product,Order,User,OrderItem

class ProductSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    
class UserSerailizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')
    
class OrderSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    
class OrderItemSerailizer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'