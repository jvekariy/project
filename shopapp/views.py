from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.core.paginator import Paginator
from django.core.mail import send_mail
# Create your views here.
def home(request):
    print("hello")
    return HttpResponse("hello")


# *********************** ABOUT *********************************

def about(request):
    if "email" in request.session:
        return render(request,"about.html")
    else:
        return render(request,"login.html")


# *************************** MEN ********************************    
    
def men(request):
    if "email" in request.session:
        pid=product.objects.all()
        pud=category.objects.all()
        
        uid=register.objects.get(email=request.session['email'])
        wid=wishlist_add.objects.filter(register=uid).order_by("-id")
        l1=[]
        for i in wid:
            l1.append(i.product.id)
        print(l1)    

        paginator=Paginator(pid,4)
        page_get=request.GET.get("page")
        pid=paginator.get_page(page_get)

        ceid=request.GET.get("ceid")
        print(ceid)
        if ceid:
            pid=product.objects.filter(category=ceid)
        pro={
            "pid":pid,
            "l1":l1,
            "pud":pud,
        }
        return render(request,"men.html",pro)
    else:
        return render(request,"login.html") 
    
    
# ***************************** CART ************************************

def cart(request):
    if "email" in request.session:
        uid=register.objects.get(email=request.session['email'])
        print(uid)
        pid=add_to_cart.objects.filter(register=uid).order_by("-id")
        l1=[]
        subtotal = 0
        shipping = 40
        for i in pid:
            l1.append(i.total)
        print(l1)
        subtotal=sum(l1)
        total=subtotal+shipping

        contaxt={
            "pid":pid,
            "l1":l1,
            "subtotal" : subtotal,
            "shipping" : shipping,
            "total" : total
        }
        return render(request,"cart.html",contaxt)
    else:
        return render(request,"login.html")
    


    
def cart_add(request,id):
    if "email" in request.session:
        uid=register.objects.get(email=request.session['email'])
        
        spid=product.objects.get(id=id)
        print(spid.product_name)
        print(spid.price)
        weid=add_to_cart.objects.filter(register=uid,product=spid).exists()
        print(weid)
        if weid:
            weid=add_to_cart.objects.get(register=uid,product=spid)
            weid.delete()
            return redirect(men)
        
        add_to_cart.objects.create(register=uid,product=spid,product_name=spid.product_name,price=spid.price,quantity=1,total=spid.price,image=spid.image)

        return redirect(cart)
    else:    
        return render(request,"login.html")
    

def cart_minus(request,id):

    seid=add_to_cart.objects.get(id=id)
    if seid.quantity >1:
        seid.quantity-=1
        seid.total=seid.price*seid.quantity
        seid.save() 
    else:
        seid.delete()
    return redirect(cart)

def cart_plus(request,id):

    seid=add_to_cart.objects.get(id=id)
    seid.quantity+=1
    seid.total=seid.price*seid.quantity

    seid.save() 
    return redirect(cart)

    
def cart_delete(request,id):

    seid=add_to_cart.objects.get(id=id)
    seid.delete() 
    return redirect(cart)

    
    
# ***************************** CHECKOUT ************************************

def checkout(request):
    if "email" in request.session:
        uid=register.objects.get(email=request.session['email'])
        pid=add_to_cart.objects.filter(register=uid).order_by("-id")
        
        l1=[]
        subtotal = 0
        shipping = 40
        for i in pid:
            l1.append(i.total)
        print(l1)
        subtotal=sum(l1)
        total=subtotal+shipping
        
        if request.POST:
            first_name=request.POST["first_name"]
            last_name=request.POST["last_name"]
            address=request.POST["address"]
            city=request.POST["city"]
            state=request.POST["state"]
            zip_code=request.POST["zip_code"]
            email=request.POST["email"]
            phone=request.POST["phone"]

            print(first_name,last_name,address,city,state,zip_code,email,phone)
            checkout_page.objects.create(first_name=first_name,last_name=last_name,address=address,city=city,state=state,zip_code=zip_code,email=email,phone=phone)
        contaxt={
            "uid":uid,
            "pid":pid, 
            "l1":l1,
            "subtotal" : subtotal,
            "shipping" : shipping,
            "total" : total
        }

        return render(request,"checkout.html",contaxt)
    else:
        return render(request,"login.html")
    



    

# ***************************** CONTACT ************************************

def contact(request):
    if "email" in request.session:
        uid=register.objects.get(email=request.session['email'])
        print(uid.email)

        if request.POST:
            first_name=request.POST["first_name"]
            last_name=request.POST["last_name"]
            email=request.POST["email"]
            subject=request.POST["subject"]
            message=request.POST["message"]

            print(first_name,last_name,email,subject,message)
            contect_message.objects.create(first_name=first_name,last_name=last_name,email=email,subject=subject,message=message)
       
        contaxt={
            "uid":uid
        }
        return render(request,"contact.html",contaxt)
    else:
        return render(request,"login.html")
    
    
# ***************************** INDEX ************************************

def index(request):
    if "email" in request.session:
        pid=product.objects.all()
        pro={
            "pid":pid
        }
        return render(request,"index.html",pro)
    else:
        return render(request,"login.html")



# ***************************** order_complete ************************************

def order_complete(request):
    if "email" in request.session:
        return render(request,"order_complete.html")
    else:
        return render(request,"login.html")
    

# ***************************** product_detail ************************************

def product_detail(request,id):
    if "email" in request.session:
        spid=product.objects.get(id=id)
        contaxt={
            "spid":spid
        }
        return render(request,"product_detail.html",contaxt)
    else:
        return render(request,"login.html")
    

# ***************************** wishlist ************************************

def wishlist(request):
    if "email" in request.session:
        uid=register.objects.get(email=request.session['email'])
        pid=wishlist_add.objects.filter(register=uid).order_by("-id")
        contaxt={
            "pid":pid
        }
        return render(request,"wishlist.html",contaxt)
    else:
        return render(request,"login.html")
    




def add_wishlist(request,id):
    if "email" in request.session:
        uid=register.objects.get(email=request.session['email'])
        spid=product.objects.get(id=id)
        print(spid.product_name)
        print(spid.price)
        seid=wishlist_add.objects.filter(register=uid,product=id).exists()
        print(seid)
        if seid:
            seid=wishlist_add.objects.get(register=uid,product=id)
            seid.delete()
            print("product exists")
        else:
            
            wishlist_add.objects.create(register=uid,product=spid,product_name=spid.product_name,price=spid.price,image=spid.image) 
        return redirect(men)    
    else:
        return render(request,"login.html")
    

def wishlist_delete(request,id):

    seid=wishlist_add.objects.get(id=id)
    seid.delete() 
    return redirect(wishlist)


    

# ***************************** women ************************************

def women(request):
    if "email" in request.session:
        return render(request,"women.html")
    else:
        return render(request,"login.html")
    


# ***************************** LOGIN ************************************    

def login(request):
    if "email" in request.session:
        return redirect(index)
    else:

        if request.POST:
            email=request.POST["email"]
            password=request.POST["password"]       
            try:
                
                uid=register.objects.get(email=email) 
                
                if password==uid.password:
                    request.session["email"]=email
                    return redirect(index)
                else:
                    print("invalide password")
                    contaxt={
                        "pmsg":"invalide password",
                        "email":email,
                        
                        
                    }
                    return render(request,"login.html",contaxt)

            except:
                print("ok")
                print(email,password)
                contaxt={
                    "msg":" invalide email",
                    "email":email,
                    "password":password,
                    
                }
                return render(request,"login.html",contaxt)
            
            
        else:  
            return render(request,"login.html")
    
            

# ***************************** register_from ************************************

def register_from(request):
    if request.POST:
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        Confirm_password=request.POST["confirm_password"]
        uid=register.objects.filter(email=email).exists()
        if uid:
            
            contaxt={
                "name":username,
                "password":password,
                "cp":Confirm_password,
                "msg":"Invalid Email"
            }   
            return render(request,"register.html",contaxt)
        else:
            if password==Confirm_password:
                print(username,email,password,Confirm_password)
                register.objects.create(username=username,email=email,password=password,Confirm_password=Confirm_password)
                return render(request,"register.html")
            else:
                print("error")
                return render(request,"register.html")
    else:
        return render(request,"register.html")

        

def logout(request):
    del request.session['email']
    return redirect(login)


# ***************************** forgate_password ************************************
import random
def forgate_password(request):
        if request.POST:
            email=request.POST["email"]
            otp=random.randint(1000,9999)
            uid=register.objects.filter(email=email).exists()
            print(uid)
            if uid:
                uid=register.objects.get(email=email)
                uid.otp=otp
                uid.save()
                send_mail("test",f"test email=============={otp}","gohiljayb10@gmail.com",[email])
                co={
                    "uid" : uid,

                } 
                return render(request,"confirm_password.html",co)
            else:
                co={
                   
                } 
                return render(request,"forgate_password.html")

            
        return render(request,"forgate_password.html")


# ***************************** confirm_password ************************************

def confirm_password(request):
        
        if request.POST:
            email=request.POST["email"]
            otp=request.POST["otp"]
            password=request.POST["password"]
            confirm_password=request.POST["confirm_password"]
            uid=register.objects.get(email=email)
            if uid.otp == int(otp):
                print("Yes")
                if password == confirm_password :
                    uid.password=password
                    uid.Confirm_password=confirm_password
                    uid.save()
                    return redirect(login)
                else:
                    contaxt={
                    "msg":"Invalid Password",
                    "uid":uid
                }
                return render(request,"confirm_password.html",contaxt)

            else:
                print("No")   
                contaxt={
                    "msg":"Invalid Otp",
                    "uid":uid
                }
                return render(request,"confirm_password.html",contaxt)


# ***************************** PROFILE ************************************

def profile(request):
    if "email" in request.session:
        uid=register.objects.get(email=request.session['email'])
        print(uid.email) 
        print(uid.username)
        if request.POST:
            username=request.POST["username"]
            s_name=request.POST["s_name"]
            email=request.POST["email"]
            education=request.POST["education"]
            address=request.POST["address"]
            phone=request.POST["phone"]
            if request.FILES:
                image=request.FILES["image"]

                uid.username=username
                uid.s_name=s_name
                uid.email=email
                uid.education=education
                uid.address=address
                uid.phone=phone
                uid.image=image
                uid.save()
            else:
                uid.username=username
                uid.s_name=s_name
                uid.email=email
                uid.education=education
                uid.address=address
                uid.phone=phone
                uid.save()


            print(username,s_name,email,education,address,phone)
        contaxt={
            "uid":uid
        }   
        return render(request,"profile_page.html",contaxt)
    else:
        return render(request,"login.html")
    

# ***************************** SEARCH ************************************

def search(request):
    # if request.POST:
    #     search=request.POST["search"]
    #     print(search)
    #     pid=product.objects.filter(product_name__contains=search)
    #     context={
    #         "pid":pid
    #     }
    #     return redirect(men,context)

    
    search=request.GET["search"]
    print(search)
    pid=product.objects.filter(product_name__contains=search)
    context={
        "pid":pid
    }
    return render(request,"men.html",context)


# ***************************** REVIEW ************************************

def review(request):
    
    if request.POST:
        rating=request.POST["rating"]
        comments=request.POST["comments"]
        
        print(rating,comments)
        user_review.objects.create(rating=rating,comments=comments)
        return redirect(index)
    return render(request,"rating.html")


# ***************************** rating ************************************   

def rating(request):
        return render(request,"rating.html")



#**************************** category ***********************

def category_page(request):
    if "email" in request.session:
        pud=category.objects.all()

        print(pud)
        pro={
                "pud":pud,               
            }
        return render(request,"men.html",pro)
    else:
        return render(request,"men.html")


  