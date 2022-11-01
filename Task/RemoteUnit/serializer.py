from rest_framework import serializers
from .models import ProductType,RUDevice,Invoice

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductType
        fields = ['url', 'id', 'Product_Name', 'created_date','updated_date']


class RUDeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RUDevice
        fields = ['url', 'Id', 'Name', 'product_type','product_price','location','created_date','updated_date']



class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Invoice
        fields = ['url', 'id', 'Device_Name', 'Product_Price','Product_Type','created_date','updated_date']

       
       