from django.contrib import admin
from .models import Cake, Cart, CartItem

admin.site.register(Cake)
admin.site.register(Cart)
admin.site.register(CartItem)
