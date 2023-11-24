from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib.auth.views import get_user_model
User = get_user_model()

from main.models import Product, Image, ProductCart


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


class GalleryView(View):
    template_name = 'gallery.html'
    context = {}

    def get(self, request):
        product_data = Product.objects.all()
        products_data = []
        for product in product_data:
            image = Image.objects.filter(product=product).first()
            product.image = image
            products_data.append(product)
        self.context.update({'product_data': products_data})
        self.context.update({'row_count': [1, 2, 3, 4]})
        return render(request, self.template_name, self.context)

    def put(self, request):
        pk = request.pk
        product = Product.objects.get(id=pk)
        user = User.objects.get()
        product_cart = ProductCart.objects.create(
            count=request.pk,
            product=product,
            user=user
        )
        product_cart.save()
        return JsonResponse({'message': 'Product successfully added to cart'})



def contact_us(request):
    return render(request, 'contact-us.html')


def cart(request):
    return render(request, 'cart.html')


class CheckoutView(View):
    template_name = 'checkout.html'
    context = {}

    def get(self, request):
        product_data = ProductCart.objects.all()
        products_data = []
        for product in product_data:
            image = Image.objects.filter(product=product).first()
            products = Product.objects.filter(product=product)
            products.image = image
            products_data.append(product)
            products_data.append(products)
        self.context.update({'product_data': products_data})
        return render(request, self.template_name, self.context)


def my_account(request):
    return render(request, 'my-account.html')


def shop(request):
    return render(request, 'shop.html')


class ShopDetailsView(View):
    template_name = 'shop-detail.html'
    context = {}

    def get(self, request):

        return render(request, self.template_name, self.context)


def wishlist(request):
    return render(request, 'wishlist.html')

# Create your views here.
