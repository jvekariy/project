from django.db import models

# Create your models here.


class register(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.TextField(max_length=50)
    Confirm_password=models.TextField(max_length=50)
    s_name=models.CharField(max_length=50,blank=True,null=True)
    education=models.CharField(max_length=50,blank=True,null=True)
    address=models.CharField(max_length=50,blank=True,null=True)
    phone=models.IntegerField(blank=True,null=True)
    image=models.ImageField(upload_to="images",blank=True,null=True)

    def __str__(self) -> str:
        return self.username
    
class product(models.Model):
    product_name=models.CharField(max_length=50)
    price=models.IntegerField()
    image=models.ImageField(upload_to='images')
    image1=models.ImageField(upload_to='images',blank=True,null=True)
    image2=models.ImageField(upload_to='images',blank=True,null=True)
    image3=models.ImageField(upload_to='images',blank=True,null=True)

    def __str__(self) -> str:
        return self.product_name
    
class contect_message(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.first_name