from django.shortcuts import render
from rest_framework import viewsets
from .models import ProductType,RUDevice,Invoice
from .serializer import ProductTypeSerializer,RUDeviceSerializer,InvoiceSerializer
from decimal import Decimal
from django.conf import settings

class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class RUDeviceViewSet(viewsets.ModelViewSet):
    queryset = RUDevice.objects.all()
    serializer_class = RUDeviceSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


