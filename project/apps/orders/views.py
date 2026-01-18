from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from apps.catalog.models import producto

def product_page(request, product_name,product_id):
    product = producto.objects.get(nombre=product_name, id = product_id)
    print(product)
    if request.method == "GET":
        
        return render(request, "orders/productpage.html", {"product": product})
    else:
        return render(request, "orders/productpage.html", {"product": product})
    