from django.urls import path
from . import views
urlpatterns = [
    path('', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('add_cart/<int:movie_id>/', views.add_cart, name='add_cart'),
    path('remove_cart_item/<int:movie_id>/<int:cart_item_id>/', views.remove_cart_item, name='remove_cart_item'),
]