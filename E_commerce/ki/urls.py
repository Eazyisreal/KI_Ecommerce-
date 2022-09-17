from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('account_dashboard/', views.account_dashboard, name='account_dashboard'),
    path('account_edit/<str:pk>', views.account_edit, name='account_edit'),
    path('account_orders/', views.account_orders, name='account_orders'),
    path('account_profile/', views.account_profile, name='account_profile'),
    path("create_profile/",views.create_profile, name="create_profile"),
    path('address/', views.address, name='address'),
    path('billing_details/', views.billing_details, name='billing_details'),
    path('blog_post/', views.blog_post, name='blog_post'),
    path('blog_read/', views.blog_read, name='blog_read'),
    path('cart/', views.cart, name='cart'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('payment_method/', views.payment_method, name='payment_method'),
    path('product_details/<str:pk>', views.product_details, name='product_details'),
    path('search/', views.search, name='search'),
    path('shop_grid/', views.shop_grid, name='shop_grid'),
    path('shop_grid_type_4/', views.shop_grid_type_4, name='shop_grid_type_4'),
    path('shop_grid_type_5/', views.shop_grid_type_5, name='shop_grid_type_5'),
    path('thank_you/', views.thank_you, name='thank_you'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('test/', views.test, name="test")
]
