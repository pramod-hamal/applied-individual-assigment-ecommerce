from django.db import models
from django.utils.text import slugify
from django.conf import settings

#make category enums 

class Product(models.Model):
    class Category(models.TextChoices): 
        ELECTRONICS = "electronics"
        FASHION = "fashion"
        HOME = "home",
        JEWELERY = "jewelry"
        MENS_CLOTHING = "mens_clothing"
        WOMENS_CLOTHING = "womens_clothing"
        UNCATEGORIZED = "Uncategorized"
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255, choices=Category.choices, default=Category.ELECTRONICS)
    image = models.ImageField(upload_to='product_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)
