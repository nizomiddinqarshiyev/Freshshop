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

    def __str__(self):
        return self.name


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pics', blank=True, null=True)


class ShoppingCart(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_at = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.service.title} from {self.user.username}'


class ProductCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_at = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.product.name} from {self.user.username}'

class Comment(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

