from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=100,verbose_name='Nomi')
    desc = models.TextField(verbose_name='Xaqida')
    image = models.ImageField(verbose_name='Rasm')
    price = models.CharField(max_length=155,verbose_name='Narxi')
    quantity = models.IntegerField(verbose_name="Qancha?")

    def __str__(self) -> str:
        return self.title


class User(models.Model):
    username = models.CharField(max_length=100,verbose_name='Username')
    email = models.EmailField(verbose_name='Email',max_length=150,unique=True)
    phone_number = models.CharField(max_length=100,verbose_name='Telefon Raqam')

    def __str__(self) -> str:
        return self.username
    


class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=15,decimal_places=2)

    

class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name="Miqdori")
    order = models.ForeignKey(Order,on_delete=models.CASCADE)    

