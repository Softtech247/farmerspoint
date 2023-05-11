from django.db import models

# Create your models here.
class ProductCagories(models.Model):
    MainCategory = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Product Categories"
    def __str__(self):
        return self.MainCategory
    

class Measurement(models.Model):
    unit = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Measurement"
    def __str__(self):
        return self.unit

class ProductSubCagories(models.Model):
    productcategory = models.ForeignKey(ProductCagories, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Product Sub Categories"
    def __str__(self):
        return self.category
    

class Products(models.Model):
    category = models.ForeignKey(ProductSubCagories, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    farm = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    unit = models.ForeignKey(Measurement, on_delete=models.CASCADE,)
    image = models.ImageField(blank=True,upload_to='assets/uploads/')
    promo = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = "Product"
    def __str__(self):
        return self.name
    