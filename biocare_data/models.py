from django.db import models
from django.utils.text import slugify
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique=True)
    category = models.CharField(max_length=100)
    # Price
    price_qty_1 = models.CharField(max_length=255)
    price_1 = models.CharField(max_length=30)
    
    price_qty_2 = models.CharField(max_length=255)
    price_2 = models.CharField(max_length=30)
    
    price_qty_3 = models.CharField(max_length=255)
    price_3 = models.CharField(max_length=30)
    
    info = models.TextField()
    shop_link = models.URLField(max_length=100)
    image = models.ImageField(upload_to='product_img')
    
    # Head and Value
    pt1_head = models.CharField(max_length=50,default='Null')
    pt1_value = models.CharField(max_length=50,default='Null')
    
    pt2_head = models.CharField(max_length=50,default='Null')
    pt2_value = models.CharField(max_length=50,default='Null')
    
    pt3_head = models.CharField(max_length=50,default='Null')
    pt3_value = models.CharField(max_length=50,default='Null')
    
    pt4_head = models.CharField(max_length=50,default='Null')
    pt4_value = models.CharField(max_length=50,default='Null')
    
    pt5_head = models.CharField(max_length=50,default='Null')
    pt5_value = models.CharField(max_length=50,default='Null')
    
    pt6_head = models.CharField(max_length=50,default='Null')
    pt6_value = models.CharField(max_length=50,default='Null')
    
    pt7_head = models.CharField(max_length=50,default='Null')
    pt7_value = models.CharField(max_length=50,default='Null')
    
    pt8_head = models.CharField(max_length=50,default='Null')
    pt8_value = models.CharField(max_length=50,default='Null')
    
    pt9_head = models.CharField(max_length=50,default='Null')
    pt9_value = models.CharField(max_length=50,default='Null')
    
    pt10_head = models.CharField(max_length=50,default='Null')
    pt10_value = models.CharField(max_length=50,default='Null')
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args,**kwargs)
        
        
class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique=True)
    date=models.DateField()
    category = models.CharField(max_length=100)
    tags = models.CharField(max_length=255)
    para_1 = models.TextField()
    para_2 = models.TextField()
    head_image = models.ImageField(upload_to='blog_img')
    secondary_image_1 = models.ImageField(upload_to='blog_img')
    secondary_image_2 = models.ImageField(upload_to='blog_img')
    views = models.CharField(default=0,max_length=100)
    
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args,**kwargs)
        
        
class Distributor(models.Model):
    user_id = models.CharField(max_length=10)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    user_mail = models.CharField(max_length=255)
    user_number = models.CharField(max_length=15)
    user_address = models.TextField()
    user_pin_code = models.CharField(max_length=8)
    user_city = models.CharField(max_length=255)
    user_state = models.CharField(max_length=255)
    user_country = models.CharField(max_length=255)
    
    # Delivery address
    delivery_mail = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    delivery_address = models.TextField()
    delivery_pin_code = models.CharField(max_length=8)
    delivery_city = models.CharField(max_length=255)
    delivery_state = models.CharField(max_length=255)
    delivery_country = models.CharField(max_length=255)
    
    accepted = models.BooleanField(default=False)