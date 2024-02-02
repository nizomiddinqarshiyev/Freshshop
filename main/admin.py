from django.contrib import admin
from .models import (Product, Service, Image, Category,
                     Comment, ShoppingCart, ProductCart, Subscriber, Wishlist, Blog, Discount)

# Register your models here.

admin.site.register((Product, Service, Image, Category,
                     Comment, ShoppingCart, ProductCart, Subscriber, Wishlist, Blog, Discount))
