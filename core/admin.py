from core.models import Product, Order, Review
from django.contrib import admin


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'product_price']

    def product_price(self, obj):
        return u'{} - ${}'.format(obj.product.name, obj.product.price)
    product_price.short_description = 'Purchase'

# Register your models here.
admin.site.register(Product)
admin.site.register(Review)