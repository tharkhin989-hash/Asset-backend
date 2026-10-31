from django.db import models

# Create your models here.
from django.db import models

class Currency(models.Model):
    currency_id = models.AutoField(primary_key=True)
    currency_code=models.CharField(max_length=3, unique=True)
    currency_name=models.CharField(max_length=50)
    currency_symbol=models.CharField(max_length=10, blank=True, null=True)
    decimal_places=models.IntegerField(default=2)
    is_functional_currency=models.BooleanField(default=False)
    is_presentation_currency=models.BooleanField(default=False)
    allow_transaction_currency=models.BooleanField(default=True)
    allow_exchange_rate_entry=models.BooleanField(default=True)
    amount_rounding_precision=models.DecimalField(max_digits=10,decimal_places=2,default=0.01)
    depreciation_rounding=models.DecimalField(max_digits=10,decimal_places=2,default=0.01)
    transaction_currency=models.ForeignKey("self",on_delete=models.SET_NULL,null=True,blank=True,related_name="transaction_currency_users")
    exchange_rate=models.DecimalField(max_digits=20,decimal_places=6,null=True,blank=True)
    functional_currency=models.ForeignKey("self",on_delete=models.SET_NULL,null=True,blank=True,related_name="functional_currency_users")
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self): return f"{self.currency_code} - {self.currency_name}"

class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    currency=models.ForeignKey(Currency,on_delete=models.PROTECT,related_name="countries",null=True,blank=True)
    country_code=models.CharField(max_length=3)
    country_name=models.CharField(max_length=100)
    iso=models.CharField(max_length=3,blank=True,null=True)
    phone=models.CharField(max_length=20,blank=True,null=True)
    default_time_zone=models.CharField(max_length=50,blank=True,null=True)
    default_language=models.CharField(max_length=20,blank=True,null=True)
    date_format=models.CharField(max_length=20,blank=True,null=True)
    allow_asset_location=models.BooleanField(default=True)
    default_country=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self): return self.country_name

class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    parent_dept=models.ForeignKey("self",on_delete=models.SET_NULL,null=True,blank=True,related_name="child_departments")
    dept_code=models.CharField(max_length=20,blank=True,null=True)
    dept_name=models.CharField(max_length=100)
    dept_short_name=models.CharField(max_length=50)
    dept_type=models.CharField(max_length=20,choices=[("HR","HR"),("IT","IT"),("FINANCE","FINANCE"),("SALES","SALES"),("MARKETING","MARKETING"),("OPERATIONS","OPERATIONS")],default="OPERATIONS")
    allow_assignment=models.BooleanField(default=True)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self): return self.dept_name

class Branch(models.Model):
    branch_id = models.AutoField(primary_key=True)
    country=models.ForeignKey(Country,on_delete=models.PROTECT,related_name="branches")
    branch_code=models.CharField(max_length=10)
    branch_name=models.CharField(max_length=100)
    region=models.CharField(max_length=100,blank=True,null=True)
    city=models.CharField(max_length=100,blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    phone=models.CharField(max_length=20,blank=True,null=True)
    email=models.EmailField(max_length=100,blank=True,null=True)
    postal_code=models.IntegerField(null=True,blank=True)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.CharField(max_length=100,blank=True,null=True)
    updated_by=models.CharField(max_length=100,blank=True,null=True)
    def __str__(self): return self.branch_name

class Custodian(models.Model):
    custodian_id = models.AutoField(primary_key=True)
    branch=models.ForeignKey(Branch,on_delete=models.PROTECT,related_name="custodians",null=True,blank=True)
    dept=models.ForeignKey(Department,on_delete=models.PROTECT,related_name="custodians",null=True,blank=True)
    custodian_code=models.CharField(max_length=10,blank=True,null=True)
    custodian_name=models.CharField(max_length=100)
    custodian_type=models.CharField(max_length=20,choices=[("SUPPLIER","SUPPLIER"),("EMPLOYEE","EMPLOYEE"),("EXTERNAL","EXTERNAL")],default="SUPPLIER")
    phone=models.CharField(max_length=20,blank=True,null=True)
    email=models.EmailField(max_length=100,blank=True,null=True)
    can_hold_assets=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self): return self.custodian_name
