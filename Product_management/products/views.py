from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product

from django.shortcuts import render
from .models import Product

def product_list(request):
    name = request.GET.get('name', '')
    product_id = request.GET.get('product_id', '')

    # Initialize query filter
    filter_args = {}
    if name:
        filter_args['name__icontains'] = name
    if product_id:
        filter_args['product_id'] = product_id

    products = Product.objects.filter(**filter_args)

    return render(request, 'product_list.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def product_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        image = request.FILES.get('image')
        
        # Handle validation and conversion here
        try:
            price = float(price)
            stock = int(stock)
        except ValueError:
            return HttpResponse("Invalid data provided", status=400)
        
        # Create the product
        Product.objects.create(
            name=name,
            description=description,
            price=price,
            stock=stock,
            image=image
        )
        return redirect('product_list')
    
    return render(request, 'product_form.html', {'action': 'Create'})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        product.name = request.POST.get('name', product.name)
        product.description = request.POST.get('description', product.description)
        try:
            product.price = float(request.POST.get('price', product.price))
            product.stock = int(request.POST.get('stock', product.stock))
        except ValueError:
            return HttpResponse("Invalid data provided", status=400)
        product.image = request.FILES.get('image', product.image)
        
        product.save()
        return redirect('product_list')
    
    return render(request, 'product_form.html', {'product': product, 'action': 'Update'})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    
    return render(request, 'product_confirm_delete.html', {'product': product})
