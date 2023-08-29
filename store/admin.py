from django.contrib import admin
from . models import Customer, Product, Order, OrderItem, ShippingAddress

admin.site.site_header = 'My Admin Area'
admin.site.index_title = 'Welcome'

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
