from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from api import views

urlpatterns = [
    path('cakes/', views.CakeList.as_view(), name="cake-list"),
    path('cart/', views.CartDetail.as_view(), name="cart"),
    path('cart/item/', views.CartItem.as_view(), name="cart_item"),
    path('cart/<int:cartitem_id>/update/', views.UpdateCart.as_view(), name="update-cartitem"),
    path('cart/<int:cartitem_id>/delete/', views.DeleteCartItem.as_view(), name="delete-cartitem"),
    path('checkout/', views.Checkout.as_view(), name="checkout"),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
