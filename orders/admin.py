from django.contrib import admin
from orders.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display=['id','customer','size','quantity','created_at','updated_at','order_status']
    list_filter=['size','created_at','order_status']


admin.site.register(Order,OrderAdmin)

