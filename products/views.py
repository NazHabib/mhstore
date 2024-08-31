from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm

from django.shortcuts import render
from .models import Product


def search_product(request):
    query = request.GET.get('q')
    sort_by = request.GET.get('sort_by')

    # Filter products based on the search query
    products = Product.objects.filter(code__icontains=query) if query else Product.objects.all()

    # Apply sorting based on the selected option
    if sort_by == 'price_asc':
        products = products.order_by('price_sell')
    elif sort_by == 'price_desc':
        products = products.order_by('-price_sell')
    elif sort_by == 'stock_asc':
        products = products.order_by('stock')
    elif sort_by == 'stock_desc':
        products = products.order_by('-stock')
    elif sort_by == 'alphabetical_asc':
        products = products.order_by('type')
    elif sort_by == 'alphabetical_desc':
        products = products.order_by('-type')

    return render(request, 'products/search.html', {'products': products})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('search_product')
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})

def update_stock(request, code):
    product = get_object_or_404(Product, code=code)
    if request.method == 'POST':
        stock_change = int(request.POST.get('stock_change'))
        product.stock += stock_change
        product.save()
        return redirect('search_product')
    return render(request, 'products/update_stock.html', {'product': product})
