from django.shortcuts import render
from rest_framework import viewsets
from .models import Currency, Country, Department, Branch, Custodian
from .serializers import CurrencySerializer, CountrySerializer, DepartmentSerializer, BranchSerializer, CustodianSerializer
class CurrencyViewSet(viewsets.ModelViewSet):
    queryset=Currency.objects.all()
    serializer_class=CurrencySerializer
class CountryViewSet(viewsets.ModelViewSet):
    queryset=Country.objects.all()
    serializer_class=CountrySerializer
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer
class BranchViewSet(viewsets.ModelViewSet):
    queryset=Branch.objects.all()
    serializer_class=BranchSerializer
class CustodianViewSet(viewsets.ModelViewSet):
    queryset=Custodian.objects.all()
    serializer_class=CustodianSerializer

# Create your views here.
