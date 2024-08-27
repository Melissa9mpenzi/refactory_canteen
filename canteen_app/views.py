from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Product, Transaction
from django.core.files.storage import FileSystemStorage
from .forms import ProductForm


#views are home page, view product, buy product, receipt page, search
# Create your views here.
def homePage(request):
    allProducts = Product.objects.all()
    context = {}
    context['allProducts'] = allProducts
    return render(request, "home.html", context)

def viewProduct(request, product_id):
    selected_product = Product.objects.get(id=product_id)
    context = {}
    context["product"] = selected_product
    return render(request, "view.html", context)

def buyProduct(request, product_id):
    selected_product = Product.objects.get(id=product_id)
    context = {}
    context["product"] = selected_product
    return render(request, "buy.html", context)

def searchProduct(request):
    if request.method == "POST":
        searched_name = request.POST['searched']
        results = Product.objects.filter(name__contains=searched_name)
        context = {}
        context['results'] = results
        return render(request, 'searchproduct.html', context)

def receiptPage(request, transaction_id):
    your_receipt = Transaction.objects.get(tx_id=transaction_id)

def image_upload(request):
    if request.method== 'POST':
        my_image = request.FILES['image']
        fs = FileSystemStorage()
        filename = 'canteen_app/static/images'+ my_image.name
        fs.save(filename, my_image)
    return render(request, 'image_upload.html')