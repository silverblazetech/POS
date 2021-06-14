from django.shortcuts import render


# Create your views here.
def home(request):
    context = {}
    return render(request, 'store/dashboard.html', context)


def dashboard(request):
    context = {}
    return render(request, 'store/dashboard.html', context)


def product(request):
    context = {}
    return render(request, 'store/product.html', context)


def customer(request):
    context = {}
    return render(request, 'store/customer.html', context)


def supplier(request):
    context = {}
    return render(request, 'store/supplier.html', context)


def sales(request):
    context = {}
    return render(request, 'store/sales.html', context)


def purchase(request):
    context = {}
    return render(request, 'store/purchase.html', context)


