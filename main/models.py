import uuid
from datetime import timezone

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Service(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.FloatField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    count = models.PositiveIntegerField(default=1)
    discount = models.ForeignKey('Discount', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pics', blank=True, null=True)


class ShoppingCart(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_at = models.DateTimeField(auto_now_add=True)
    count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.service.title} from {self.user.username}'


class ProductCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_at = models.DateTimeField(auto_now_add=True)
    count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.product.name} from {self.user.username}'


class Comment(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_stock = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{str(self.product)} from {self.user}'


class Discount(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    discount = models.PositiveIntegerField()
    starting_date = models.DateField()
    ending_date = models.DateField()

    def __str__(self):
        return f'{self.name}'


class Subscriber(models.Model):
    email = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.email}'


class Blog(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pics/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} from {self.user}'


