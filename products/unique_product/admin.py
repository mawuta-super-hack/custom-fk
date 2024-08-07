from django.contrib import admin

from .models import Attr, Product, ProductAttr, UniqueProduct

admin.site.register(Product)
admin.site.register(Attr)
admin.site.register(UniqueProduct)
admin.site.register(ProductAttr)
