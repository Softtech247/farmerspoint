from django.shortcuts import render
from django.contrib.auth.models import User

from coreapp.models import *

# Create your views here.

def index(request):
    return render(request,"index.html")

def products(request):

    categorylist = []
    livestocklist = []
    categories = ProductCagories.objects.all()
    products = Products.objects.filter(promo = False)
    for category in categories:
        subcategories = ProductSubCagories.objects.filter(productcategory=category)
        subcategorylist = [(subcategory.id, subcategory.category) for subcategory in subcategories]
        categorylist.append((category.MainCategory, subcategorylist))
    categorydict = dict(categorylist)
    promo_products = Products.objects.filter(promo = True)
    livestock_cat = ProductCagories.objects.filter(MainCategory= "Livestocks").first()
    livestock_cat_sub = ProductSubCagories.objects.filter(productcategory = livestock_cat.pk)
    for Productcategory in livestock_cat_sub:
        livestock_cate = Products.objects.filter(category_id = Productcategory.pk).first()
        if livestock_cate:
          livestocklist.append(livestock_cate)  
    
    print("livestocklist",livestocklist)
   # livestock_categorydict = dict(livestocklist)
    #print(livestock_categorydict)
    return render(request,"products.html",{"categorydict": categorydict,
                                            "products": products,"promo_products":promo_products,
                                            "livestock_products":livestocklist})

def register(request):
    if request.method == "POST": 
        email = request.POST.get('email')
        username = email.split('@')[0]
        username = username.replace('.','_')
        print(username)
        context = {}
        context['email'] = request.POST.get('email')
        context['firstname'] = request.POST.get('firstname')
        context['lastname'] = request.POST.get('lastname')

        if User.objects.filter(email=email).exists():
            context['alert'] = f"Email {email} already exist!"
            return render(request,"register.html", context=context)
    
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            context['alert'] = "Password does not match!"
            return render(request,"register.html", context=context)
        else:
            user = User.objects.create( username=username, email= email,
                                    password= request.POST.get('password1'),
                                      first_name = request.POST.get('firstname'), last_name = request.POST.get('lastname'))
            user.save()
        





    return render(request,"register.html")
