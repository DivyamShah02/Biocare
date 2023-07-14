from django.contrib import admin
from biocare_data.models import Product,Blog,Distributor

# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ('title','slug','category','shop_link')
admin.site.register(Product,AdminProduct)

class AdminBlog(admin.ModelAdmin):
    list_display = ('title','slug','views','category')
admin.site.register(Blog,AdminBlog)

class AdminDistributor(admin.ModelAdmin):
    list_display = ('first_name','last_name','company_name','user_mail','delivery_state','delivery_country','accepted')
admin.site.register(Distributor,AdminDistributor)
