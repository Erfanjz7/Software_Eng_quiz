from django.contrib import admin

from main.models import Category, Product, OrderItem

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(OrderItem)
