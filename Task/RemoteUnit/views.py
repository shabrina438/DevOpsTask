from django.shortcuts import render
from rest_framework import viewsets
from .models import ProductType,RUDevice,Invoice
from .serializer import ProductTypeSerializer,RUDeviceSerializer,InvoiceSerializer
from decimal import Decimal
from django.conf import settings
from sslcommerz_lib import SSLCOMMERZ
from django.shortcuts import redirect
 
class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
 
 
class RUDeviceViewSet(viewsets.ModelViewSet):
    queryset = RUDevice.objects.all()
    serializer_class = RUDeviceSerializer
 
 
class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
 
 
settings = {'store_id': 'store6356416cd2b40', 'store_pass': 'store6356416cd2b40@ssl', 'issandbox': True}
sslcz = SSLCOMMERZ(settings)
post_body = {}
post_body['tran_id'] = '5E121A0D01F92'
post_body['val_id'] = '200105225826116qFnATY9sHIwo'
post_body['amount'] = "10.00"
post_body['card_type'] = "VISA-Dutch Bangla"
post_body['store_amount'] = "9.75"
post_body['card_no'] = "418117XXXXXX6675"
post_body['bank_tran_id'] = "200105225825DBgSoRGLvczhFjj"
post_body['status'] = "VALID"
post_body['tran_date'] = "2020-01-05 22:58:21"
post_body['currency'] = "BDT"
post_body['card_issuer'] = "TRUST BANK, LTD."
post_body['card_brand'] = "VISA"
post_body['card_issuer_country'] = "Bangladesh"
post_body['card_issuer_country_code'] = "BD"
post_body['store_id'] = "test_testemi"
post_body['verify_sign'] = "d42fab70ae0bcbda5280e7baffef60b0"
post_body['verify_key'] = "amount,bank_tran_id,base_fair,card_brand,card_issuer,card_issuer_country,card_issuer_country_code,card_no,card_type,currency,currency_amount,currency_rate,currency_type,risk_level,risk_title,status,store_amount,store_id,tran_date,tran_id,val_id,value_a,value_b,value_c,value_d"
post_body['verify_sign_sha2'] = "02c0417ff467c109006382d56eedccecd68382e47245266e7b47abbb3d43976e"
post_body['currency_type'] = "BDT"
post_body['currency_amount'] = "10.00"
post_body['currency_rate'] = "1.0000"
post_body['base_fair'] = "0.00"
post_body['value_a'] = ""
post_body['value_b'] = ""
post_body['value_c'] = ""
post_body['value_d'] = ""
post_body['risk_level'] = "0"
post_body['risk_title'] = "Safe"
if sslcz.hash_validate_ipn(post_body):
        response = sslcz.validationTransactionOrder(post_body['val_id'])
        print(response)
else:
        print("Hash validation failed")
 
 



