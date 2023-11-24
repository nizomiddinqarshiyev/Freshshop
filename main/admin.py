from django.contrib import admin
from .models import (Product, Service, Image, Category,
                     Comment, ShoppingCart, ProductCart)

# Register your models here.

admin.site.register((Product, Service, Image, Category,
                     Comment, ShoppingCart, ProductCart))
