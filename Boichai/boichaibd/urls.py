from django.urls import path
from boichaibd import views

urlpatterns = [

    # path('',views.base,name='base'),
    path('', views.home, name='home'),
    path('index', views.home, name='index'),
    path('product-details', views.product_details, name='product-details'),
    path('about', views.about, name='about'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('checkout', views.checkout, name='checkout'),
    path('shop', views.shop, name='shop'),
    path('blog', views.blog, name='blog'),
    path('blog-details', views.blog_details, name='blog-details'),
    path('cart', views.cart, name='cart'),
    path('contact', views.contact, name='contact'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('404', views.error, name='error'),

]
