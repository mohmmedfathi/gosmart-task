from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('person.urls')),
    path('products/', include('product.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('order.urls')),
]
