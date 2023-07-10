from django.contrib import admin

# Register your models here.
from .models import Product,Customer,Cart,Payment,OrderPlaced,WishList


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','discounted_price','category','product_image']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','locality','city','state','zipcode']

@admin.register(Cart)
class CartAdminModel(admin.ModelAdmin):
    list_display=['id','user','product','quantity']

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display=['id','user','razorpay_order_id','razorpay_payment_status','razorpay_payment_id','paid']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display=['id','user','customer','product','quantity','ordered_date','status','payment']

@admin.register(WishList)
class WishListModelAdmin(admin.ModelAdmin):
    list_display=['user','product']


admin.site.site_header="Ecom Products"
admin.site.site_title="Ecom Products"
admin.site.site_index_title="Welcome to Ecom Products"