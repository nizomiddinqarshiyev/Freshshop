from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from main.views import (
    home, about, cart, CheckoutView, contact_us,
    GalleryView, my_account, WishListView, ShopView, ShopDetailsView, IncrementCountAPIView,
    DecrementCountAPIView, ChangeCountAPIView, SubscribeAPIView, AddToCartAPIView
)

urlpatterns = [
    path("", home),
    path("about/", about),
    path("cart/", cart),
    path("contact_us/", contact_us),
    path("gallery/", GalleryView.as_view(), name="gallery"),
    path("my_account/", my_account),
    path("wishlist/", WishListView.as_view(), name="wishlist"),
    path("shop/", ShopView.as_view(), name="sidebars_shop"),
    path("shop_detail/", ShopDetailsView.as_view(), name="shop_detail"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),


    # API
    path('increment', csrf_exempt(IncrementCountAPIView.as_view()), name='increment'),
    path('decrement', csrf_exempt(DecrementCountAPIView.as_view()), name='decrement'),
    path('change', csrf_exempt(ChangeCountAPIView.as_view()), name='change'),
    path('subscribe', csrf_exempt(SubscribeAPIView.as_view()), name='subscribe'),
    path('add_cart', csrf_exempt(AddToCartAPIView.as_view()), name='add_cart')
]


