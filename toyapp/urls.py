
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('register',views.reg),
    path('login',views.log),
    path('users',views.users),
    path('edit/<int:pk>',views.edit, name='edit'),
    path('dlt/<int:pk>',views.delete,name='dlt'),
    path('prod',views.products),
    path('toys',views.toys),
    path('cart/<int:pk>',views.addcart,name='addtocart'),
    path('viewcart',views.viewcart),
    path('deletecart/<int:pk>',views.deletecart,name='deletecart'),
    path('mail',views.mail),
    path('formview',views.formview),

]