from django.shortcuts import render


# Create your views here.


def base(request):
    return render(request, 'base.html')


def home(request):
    return render(request, 'index.html')


def product_details(request):
    return render(request, 'product-details.html')


def about(request):
    return render(request, 'about.html')


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def checkout(request):
    return render(request, 'checkout.html')


def shop(request):
    return render(request, 'shop.html')


def blog(request):
    return render(request, 'blog.html')


def blog_details(request):
    return render(request, 'blog-details.html')


def cart(request):
    return render(request, 'cart.html')


def contact(request):
    return render(request, 'contact.html')

def wishlist(request):
    return render(request, 'wishlist.html')


def error(request):
    return render(request, '404.html')
