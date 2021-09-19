from django.shortcuts import render, get_object_or_404
from .models import WishList
from .forms import ProductForm
from datetime import datetime

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def list_page(request, pk):
    wishlist = get_object_or_404(WishList, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST)
        instance_product=form.save()
        product = form.save()
        wishlist.product.add(product)
        wishlist.save()
    else:
        form = ProductForm()

    return render(
        request,
        'wish_list.html',
            {
                'wishlist': wishlist,
                'is_owner_list': wishlist.owner == request.user,
                'form': form
            }
        )