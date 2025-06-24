from django.db import models

# Create your models here.
class Reg_tbl(models.Model):
    mail = models.EmailField(max_length=25)
    psw = models.CharField(max_length=16)
    cpsw = models.CharField(max_length=16)
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    gender = models.CharField(max_length=6)
    loc = models.CharField(max_length=16)

class products_tbl(models.Model):
    tname = models.CharField(max_length=25)
    tprice = models.IntegerField()
    tdes = models.TextField()
    timg = models.FileField(upload_to='pic')

class Cart_tbl(models.Model):
    user = models.ForeignKey(Reg_tbl,on_delete=models.CASCADE)
    product = models.ForeignKey(products_tbl,on_delete=models.CASCADE)
    qty = models.PositiveBigIntegerField(default=1)