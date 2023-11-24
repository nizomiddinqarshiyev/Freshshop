from django.urls import path
from main.views import (
    home, about, cart, CheckoutView, contact_us,
    GalleryView, my_account, wishlist, shop, ShopDetailsView
)

urlpatterns = [
    path("", home),
    path("about/", about),
    path("cart/", cart),
    path("contact_us/", contact_us),
    path("gallery/", GalleryView.as_view(), name="gallery"),
    path("my_account/", my_account),
    path("wishlist/", wishlist),
    path("shop/", shop),
    path("shop_detail/", ShopDetailsView.as_view(), name="shop_detail"),
    path("checkout/", CheckoutView.as_view(), name="checkout")
]


