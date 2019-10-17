from django.db import models

# Create your models here.

class Category(models.Model):
    cat_id = models.AutoField(primary_key='true')
    cat_name = models.CharField(max_length=100, null= False)
    parentID = models.IntegerField(null= False)
    class Meta:
        db_table = "category"

class Product(models.Model):
    id = models.AutoField(primary_key='true')
    name = models.CharField(max_length=100, null= False)
    cat_id = models.IntegerField(null= False)
    parentID_ID = models.IntegerField(null= False)
    price = models.FloatField(null= False)
    sale_price = models.FloatField(null= True)
    image = models.CharField(max_length= 100, null= True)
    content = models.TextField(max_length= 1000, null= True)
    class Meta:
        db_table = "product"

class Img_pro(models.Model):
    img_id = models.AutoField(primary_key='true')
    pro_id = models.IntegerField(null= False)
    img_link = models.CharField(max_length= 255, null= False)
    class Meta:
        db_table = "img_pro"

class order(models.Model):
    order_id = models.AutoField(primary_key='true')
    order_total = models.FloatField(null= False)
    order_payment = models.IntegerField(null= False)
    customer_id = models.IntegerField(null= False)
    class Meta:
        db_table = "order"

class order_detail(models.Model):
    detail_id = models.AutoField(primary_key='true')
    order_id = models.IntegerField(null= False)
    pro_id = models.IntegerField(null= False)
    quantity = models.IntegerField(null= False)
    price = models.FloatField(null= False)
    sale_price = models.FloatField(null= True)
    class Meta:
        db_table = "order_detail"

class customer(models.Model):
    cus_id = models.AutoField(primary_key='true')
    cus_name = models.CharField(max_length= 100, null= False)
    cus_email = models.CharField(max_length = 100, null= False)
    cus_phone = models.CharField(max_length= 12, null= False)
    class Meta:
        db_table = "customer"

class user(models.Model):
    id = models.AutoField(primary_key='true')
    name = models.CharField(max_length=50, null = False)
    email = models.CharField(max_length=50, null = False)
    password = models.CharField(max_length=50, null = False)
    first_name = models.CharField(max_length=50, null = True)
    last_name = models.CharField(max_length=50, null = True)
    phone = models.CharField(max_length=12, null = True)
    class Meta:
        db_table = "user"

class admin(models.Model):
	id = models.AutoField(primary_key='true')
	name = models.CharField(max_length=255,null = False)
	email =  models.CharField(max_length=255,null = False)
	password = models.CharField(max_length=255,null = False)
	class Meta:
		db_table = "admin"

class user_contacts(models.Model):
    id = models.AutoField(primary_key='true')
    name = models.CharField(max_length= 100, null= False)
    email = models.CharField(max_length= 100, null= False)
    contact = models.TextField(null = False)
    class Meta:
        db_table = "user_contact"
