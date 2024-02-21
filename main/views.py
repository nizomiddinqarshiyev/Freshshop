import datetime
import json
from datetime import timedelta

from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views import View
from django.views.generic import UpdateView
from django.contrib.auth.views import get_user_model
User = get_user_model()

from main.models import Product, Image, ProductCart, ShoppingCart, Subscriber, Wishlist


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


class ShopView(View):
    template_name = 'shop.html'
    context = {}

    def get(self, request):
        three_days_ago = datetime.datetime.now() - timedelta(days=3)
        product_new = Product.objects.filter(created_at__range=[three_days_ago, datetime.datetime.utcnow()]).all()
        # product_discount = Product.objects.filter(discount__gt=0)
        # product_data = []
        # for i in product_discount:
        #     image = Image.objects.filter(product=i).first()
        #     i.image = image
        #     product_data.append(i)
        #     i.dis_price = i.price*(100 - i.discount)/100
        product_new_data = []
        for i in product_new:
            image = Image.objects.filter(product=i).first()
            i.image = image
            product_new_data.append(i)
        # self.context.update({'product_data': product_data})
        self.context.update({'product_new': product_new_data})
        print(product_new_data)

        return render(request, self.template_name, context=self.context)


class ShopDetailsView(View):
    template_name = 'shop-detail.html'
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)


class IncrementCountAPIView(View):

    def post(self, request):
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            shopping_cart_id = json_data.get('id')
            shopping_cart = ShoppingCart.objects.get(pk=shopping_cart_id)
            shopping_cart.count += 1
            shopping_cart.save()
        except Exception as e:
            return JsonResponse({'success': False, 'error': e})
        return JsonResponse({'success': True})


class DecrementCountAPIView(View):

    def post(self, request):
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            shopping_cart_id = json_data.get('id')
            shopping_cart = ShoppingCart.objects.get(pk=shopping_cart_id)
            if shopping_cart.count > 0:
                shopping_cart.count -= 1
                shopping_cart.save()
        except Exception as e:
            return JsonResponse({'success': False, 'error': e})
        return JsonResponse({'success': True})


class ChangeCountAPIView(View):

    def post(self, request):
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            shopping_cart_id = json_data.get('id')
            product_count = json_data.get('product_count')

            shopping_cart = ShoppingCart.objects.get(pk=shopping_cart_id)
            if product_count is not None:
                shopping_cart.count = product_count
                shopping_cart.save()
        except Exception as e:
            return JsonResponse({'success': False, 'error': e})
        return JsonResponse({'success': True})


class WishListView(View):
    template_name = 'wishlist.html'
    context = {}

    def get(self, request):
        try:
            user = request.user
            wishlist = Wishlist.objects.filter(user=user)
            if wishlist is not None:
                product_data = []
                for w in wishlist:
                    product = Product.objects.get(id=w.product_id)
                    image = Image.objects.filter(product=product).first()
                    product.image = image
                    product.is_stock = w.is_stock
                    product_data.append(product)
                self.context.update({'wishlist': product_data})
                return render(request, self.template_name, self.context)
            else:
                self.context.update({'wishlist': None})
                return render({request, self.template_name, self.context})
        except Exception as e:
            return render(request, self.template_name, self.context)

# Create your views here.


class SubscribeAPIView(View):
    template_name = 'base.html'
    context = {}

    def post(self, request):

        try:
            json_data = json.loads(request.body.decode('utf-8'))
            email_data = json_data.get('email')
            if not Subscriber.objects.filter(email=email_data):
                subscriber = Subscriber.objects.create(
                    email=email_data
                )
                subscriber.save()
                self.context.update({'message': 'Successfully subscribed!'})
            else:
                self.context.update({'message': 'Email already subscribed'})
            return JsonResponse(self.context, status=200)
        except Exception as e:
            return JsonResponse({'success': False, 'error': e})


class AddToCartAPIView(View):


    def post(self, request, product_id):
        try:
            if product_id is None:
                return JsonResponse({'error': 'Product ID is required'}, status=400)

            if not request.user.is_authenticated:
                return JsonResponse('Not logged in', status=401)
            else:
                product = Product.objects.get(id=product_id)
                cart = ProductCart.objects.create(
                    product=product,
                    user=request.user,
                )
                cart.save()
                return JsonResponse({'message': 'Successfully added!'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    # def post(self, request, product_id):
    #     print(product_id)
    #     if not request.user.is_authenticated:
    #         return JsonResponse('Not logged in', status=401)
    #     else:
    #         product = Product.objects.get(id=product_id)
    #         cart = ProductCart.objects.create(
    #             product=product,
    #             user=request.user,
    #         )
    #         cart.save()
    #         return JsonResponse({'message': 'Successfully added!'}, status=200)

    def delete(self, request, product_id):
        if not request.user.is_authenticated:
            return JsonResponse('Not logged in', status=401)
        else:
            product = Product.objects.get(id=product_id)
            cart = ProductCart.objects.get(product=product)
            cart.delete()
            cart.save()
            return JsonResponse({'Cart deleted!'}, status=200)




