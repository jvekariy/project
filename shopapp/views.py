from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    return HttpResponse("hello")


def about(request):
    if "email" in request.session:
        return render(request,"about.html")
    else:
        return render(request,"login.html")

def men(request):
    if "email" in request.session:
        pid=product.objects.all()

        

        paginator=Paginator(pid,4)
        page_get=request.GET.get("page")
        pid=paginator.get_page(page_get)
        pro={
            "pid":pid
        }
        return render(request,"men.html",pro)
    else:
        return render(request,"login.html") 

def cart(request):
    if "email" in request.session:
        return render(request,"cart.html")
    else:
        return render(request,"login.html")

def checkout(request):
    if "email" in request.session:
        return render(request,"checkout.html")
    else:
        return render(request,"login.html")

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

def index(request):
    if "email" in request.session:
        pid=product.objects.all()
        pro={
            "pid":pid
        }
        return render(request,"index.html",pro)
    else:
        return render(request,"login.html")




def order_complete(request):
    if "email" in request.session:
        return render(request,"order_complete.html")
    else:
        return render(request,"login.html")


def product_detail(request,id):
    if "email" in request.session:
        spid=product.objects.get(id=id)
        contaxt={
            "spid":spid
        }
        return render(request,"product_detail.html",contaxt)
    else:
        return render(request,"login.html")

def wishlist(request):
    if "email" in request.session:
        return render(request,"wishlist.html")
    else:
        return render(request,"login.html")

def women(request):
    if "email" in request.session:
        return render(request,"women.html")
    else:
        return render(request,"login.html")
    
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


