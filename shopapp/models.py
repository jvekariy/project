from django.db import models

# Create your models here.


class register(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.TextField(max_length=50)
    otp=models.IntegerField(blank=True,null=True)
    Confirm_password=models.TextField(max_length=50)
    s_name=models.CharField(max_length=50,blank=True,null=True)
    education=models.CharField(max_length=50,blank=True,null=True)
    address=models.CharField(max_length=50,blank=True,null=True)
    phone=models.IntegerField(blank=True,null=True)
    image=models.ImageField(upload_to="images",blank=True,null=True)

    def __str__(self) -> str:
        return self.username
    
class category(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images',blank=True,null=True)


    def __str__(self) -> str:
        return self.name
        
class product(models.Model):
    category=models.ForeignKey(category,on_delete=models.CASCADE,blank=True,null=True)
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
    
class user_review(models.Model):
    rating=models.IntegerField(choices=[(i,i) for i in range (1,6)])
    comments=models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.rating}"
    


class wishlist_add(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE,blank=True,null=True)
    register=models.ForeignKey(register,on_delete=models.CASCADE,blank=True,null=True)
    image=models.ImageField(upload_to='images')
    product_name=models.CharField(max_length=50)
    price=models.IntegerField()

    def __str__(self) -> str:
        return self.product_name
    
class add_to_cart(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE,blank=True,null=True)
    register=models.ForeignKey(register,on_delete=models.CASCADE,blank=True,null=True)
    image=models.ImageField(upload_to='images')
    product_name=models.CharField(max_length=50)
    price=models.IntegerField()
    quantity=models.IntegerField()
    total=models.IntegerField()

    def __str__(self) -> str:
        return self.product_name
    
class checkout_page(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip_code=models.IntegerField()
    email=models.EmailField(max_length=50)
    phone=models.IntegerField()

    def __str__(self) -> str:
        return self.email
    







