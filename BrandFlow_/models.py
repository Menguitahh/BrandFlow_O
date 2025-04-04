from django.db import models

# Create your models here.
class User(models.Model):
    iduser = models.AutoField(primary_key=True)
    password = models.CharField(max_length=100,)
    email = models.EmailField(max_length=100,)
    phone = models.CharField(max_length=15,)
    addres = models.CharField(max_length=100,)
    username = models.CharField(max_length=100,)
    
    def __str__(self):
        return self.username
# class Order(models.Model):
#     idorder = models.AutoField(primary_key=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product_name = models.CharField(max_length=100,)
#     order_date = models.DateField(auto_now_add=True)
#     status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')])
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
#     def __str__(self):
#         return f"Order {self.id} by {self.user.username}"
    
# class Campaingn(models.Model):
#     idcampaingn = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100,)
#     start_date = models.DateField()
#     description = models.TextField()
#     end_date = models.DateField()
#     budget = models.DecimalField(max_digits=10, decimal_places=2)
#     status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('Inactive', 'Inactive'),('Complete', 'Complete'), ('Cancelled', 'Cancelled')])
    
#     def __str__(self):
#         return self.name
    
# class CampaignUser(models.Model):
#     idCampaignUser = models.AutoField(primary_key=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     campaign = models.ForeignKey(Campaingn, on_delete=models.CASCADE)
#     rol = models.CharField(max_length=100,choices= [('Admin', 'Admin'), ('User', 'User')])
#     asigned_date = models.DateField(auto_now_add=True)
    
# class Category(models.Model):
#     idcategory = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100,)
#     description = models.TextField()
    
#     def __str__(self):
#         return self.name

