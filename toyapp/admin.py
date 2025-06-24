from django.contrib import admin
from . models import Reg_tbl
from . models import products_tbl,Cart_tbl
# Register your models here.

admin.site.register(Reg_tbl)
admin.site.register(products_tbl)
admin.site.register(Cart_tbl)