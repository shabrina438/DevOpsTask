from django.db import models

# Create your models here.

class ProductType(models.Model):
    id = models.CharField(primary_key=True,max_length=255)
    Product_Name = models.CharField('Product Name',max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id


class RUDevice(models.Model):
    Id = models.CharField(primary_key=True,max_length=255)
    Name = models.CharField('Name',max_length=255)
    product_type = models.ForeignKey(ProductType, blank=True,null = True,on_delete =models.CASCADE)
    product_price = models.CharField('product price',max_length=255)
    location = models.CharField('location',max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.id


class Invoice(models.Model):
    id = models.CharField(primary_key=True,max_length=255)
    Device_Name = models.CharField('Device Name',max_length=255)
    Product_Price = models.CharField('product price',max_length=255)
    Product_Type = models.CharField('product type',max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Device_Name




