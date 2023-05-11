from django.shortcuts import render

from coreapp.models import *

# Create your views here.

def index(request):
    return render(request,"index.html")

def products(request):
    categorylist = []
    categories = ProductCagories.objects.all()
    products = Products.objects.filter(promo = False)
    for category in categories:
        subcategories = ProductSubCagories.objects.filter(productcategory=category)
        subcategorylist = [(subcategory.id, subcategory.category) for subcategory in subcategories]
        categorylist.append((category.MainCategory, subcategorylist))
    categorydict = dict(categorylist)
    promo_products = Products.objects.filter(promo = True)
    print(categorydict)
    return render(request,"products.html",{"categorydict": categorydict,
                                            "products": products,
                                            "promo_products":promo_products})