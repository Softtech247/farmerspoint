from django.contrib import admin

from coreapp.models import *

class products(admin.ModelAdmin):
    list_display = ('id','name','farm','price','unit')
    search_fields = ('name',)
    list_filter = ('farm',)
    filter_horizontal = ()   
    fieldsets = ()
admin.site.register(Products,products )


class productSubCat(admin.ModelAdmin):
    list_display = ('id','category',)
    search_fields = ()
    list_filter = ()
    filter_horizontal = ()   
    fieldsets = ()
admin.site.register(ProductSubCagories,productSubCat)


class TopProductsCat(admin.ModelAdmin):
    list_display = ('id','MainCategory',)
    search_fields = ()
    list_filter = ()
    filter_horizontal = ()   
    fieldsets = ()
admin.site.register(ProductCagories,TopProductsCat )


class measurement(admin.ModelAdmin):
    list_display = ('id','unit',)
    search_fields = ()
    list_filter = ()
    filter_horizontal = ()   
    fieldsets = ()
admin.site.register(Measurement,measurement)
