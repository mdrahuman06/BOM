from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, BOMItem
from .forms import ProductForm, BOMItemForm

# views.py

def product_list(request):
    products = Product.objects.all()
    for product in products:
        product.total_cost = sum(item.price * item.quantity for item in product.bom_items.all())
    return render(request, 'bom_app/product_list.html', {'products': products})

# def calculate_selected(request):
#     if request.method == 'POST':
#         ids = request.POST.getlist('selected_products')
#         selected_products = Product.objects.filter(id__in=ids)
#         grand_total = 0
#         for product in selected_products:
#             for item in product.bom_items.all():
#                 grand_total += item.quantity * item.price
#         return render(request, 'bom_app/calculate_result.html', {
#             'products': selected_products,
#             'grand_total': grand_total
#         })
#     return redirect('product_list')
def calculate_selected(request):
    if request.method == 'POST':
        ids = request.POST.getlist('selected_products')
        selected_products = Product.objects.filter(id__in=ids)

        products_with_totals = []
        overall_grand_total = 0

        for product in selected_products:
            bom_items = product.bom_items.all()
            product_total = sum(item.quantity * item.price for item in bom_items)
            overall_grand_total += product_total

            products_with_totals.append({
                'product': product,
                'bom_items': bom_items,
                'product_total': product_total
            })

        return render(request, 'bom_app/calculate_result.html', {
            'products_with_totals': products_with_totals,
            'grand_total': overall_grand_total
        })
    return redirect('product_list')


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    bom_items = product.bom_items.all()
    return render(request, 'bom_app/product_detail.html', {'product': product, 'bom_items': bom_items})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'bom_app/add_product.html', {'form': form})

def add_bom_item(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = BOMItemForm(request.POST)
        if form.is_valid():
            bom_item = form.save(commit=False)
            bom_item.product = product
            bom_item.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = BOMItemForm()
    return render(request, 'bom_app/add_bom_item.html', {'form': form, 'product': product})
