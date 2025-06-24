from django.shortcuts import render,redirect
from . models import Reg_tbl,products_tbl,Cart_tbl
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from . forms import regform


# Create your views here.
def index(req):
    return render(req,"index.html")

def reg(req):

    if req.method=='POST':
      
      email = req.POST.get('email')
      passw = req.POST.get('password')
      cpassw = req.POST.get('cpassword')
      fnm= req.POST.get('firstname')
      lnm= req.POST.get('lastname')
      fm = req.POST.get('r1')
      loc= req.POST.get('country')

      obj = Reg_tbl.objects.create(mail=email,psw=passw,cpsw=cpassw,fname=fnm,lname=lnm,gender=fm,loc=loc)
      obj.save()

      if obj:
         return redirect("/login")
      else:
         return render(req,"register.html")
      

    return render(req,"register.html")

def log(req):
    if req.method=='POST':
       email = req.POST.get('email')
       passw = req.POST.get('password')

       obj = Reg_tbl.objects.filter(mail=email,psw=passw)

       if obj:
          req.session['eml'] = email
          req.session['pasw'] = passw

          # for filtering the specific id 
          for i in obj:
             idno = i.id
          req.session['idn'] = idno

          return render(req,"index.html")
       
       else:
         msg = "invalid credentials"
         return render(req,"login.html",{"error":msg})
       
    return render(req,"login.html")


def users(request):
   obj = Reg_tbl.objects.all()
   return render(request,"users.html",{"users":obj})

def edit(request,pk):
   obj = Reg_tbl.objects.filter(id=pk)
   if request.method=="POST":
      eml = request.POST.get('ml')
      idl = request.POST.get('idl')
      psw = request.POST.get('ps')
      fnm = request.POST.get('fn')
      lnm = request.POST.get('ln')
      gnr = request.POST.get('gr')
      lct = request.POST.get('lc')

      obb = Reg_tbl.objects.filter(id=idl)
      obb.update(mail=eml, psw=psw, fname=fnm, lname=lnm, gender=gnr, loc=lct)
      return redirect('/users')
   return render(request,"user.html",{"user":obj})

def delete(request,pk):
   obj = Reg_tbl.objects.filter(id=pk)
   obj.delete()
   return redirect('/users')

def products(req):
   if req.method == "POST":
      tnm = req.POST.get("Tn")
      tprc = req.POST.get("Tp")
      tds = req.POST.get("Des")
      tim = req.FILES.get("Ti")
      obj = products_tbl.objects.create(tname=tnm,tprice=tprc,tdes=tds,timg=tim)
      obj.save()
      if obj:
         return render(req,"products.html",{"msg":"Details Added Successfully"})
   return render(req,"products.html")


def toys(req):
   obj = products_tbl.objects.all()
   return render(req,"toy.html",{"toys":obj})

def addcart(req,pk):
   pobj= products_tbl.objects.get(id=pk)
   idno = req.session['idn']
   uobj = Reg_tbl.objects.get(id=idno)
   cartitem,created = Cart_tbl.objects.get_or_create(user=uobj,product=pobj)
   if not created:
      cartitem.qty+=1
      cartitem.save()
   messages.success(req,"Item Added to Cart")
   return redirect("/toys")

def viewcart(req):
   idno = req.session['idn']
   cobj = Reg_tbl.objects.get(id=idno)
   cartuser = Cart_tbl.objects.filter(user=cobj)
   if cartuser:
      total_price = 0
      for i in cartuser:
         prod_prc = i.product.tprice*i.qty
         total_price += prod_prc

      return render(req,"cart.html",{"total":total_price, "cart":cartuser})
   else:
      return render(req,"cart.html",{'info':"Your cart is EMPTY"})
   

def deletecart(req,pk):
   obj = Cart_tbl.objects.filter(id=pk)
   obj.delete()

   return redirect("/viewcart")

def mail(request):
   if request.method == "POST":
      ToEml = request.POST.get("email")
      Sub = request.POST.get("sub")
      Msg = request.POST.get("text")

      send_mail(Sub,Msg,settings.EMAIL_HOST_USER,[ToEml],fail_silently=False)
      return render(request,"email.html",{"success":"MAIL SEND SUCCESSFULLY.."})

   return render(request,"email.html")

def formview(req):
   form = regform()
   if req.method =="POST":
        form=regform(req.POST)
        if form.is_valid():
            f =form.cleaned_data.get("fname")
            l = form.cleaned_data.get("lname")
            p = form.cleaned_data.get("pswd")
            c = form.cleaned_data.get("cpswd")
            e =form.cleaned_data.get("email")
            g =form.cleaned_data.get("gender")
            lo = form.cleaned_data.get("location")
            obj = Reg_tbl.objects.create(fname=f,lname=l,psw=p,cpsw=c,mail=e,gender=g,location=lo)
            obj.save()
            if obj:
                msg= "Registered successfully..."
                return render(req,"forms.html",{"form":form,"success":msg})
   return render(req,"forms.html",{"form":form})