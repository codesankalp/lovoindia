from django.urls import path, include
from . import views

urlpatterns = [
    path('shop_detail', views.shop, name='shop_detail'),
    path('cart', views.cart, name='cart'),
    path('shop', views.grid, name='grid'),
    path('contact', views.contact, name='contact'),
    path('', views.home, name='home'),
    path('', include('social_django.urls')),
    path('profile/', views.profile,name='profile'),
    path('logout/', views.logout),
    path('register/', views.register),
    path('productregister/', views.product_register,name='product-register'),
    path('subscribe/',views.subscribe,name='subscribed'),
]


