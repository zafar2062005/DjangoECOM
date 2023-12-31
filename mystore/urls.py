from django.urls import path
from mystore import views

urlpatterns =[
    path('' ,views.index , name='index'),
    path('about.html/' ,views.about , name='about'),
    path('contact.html/' ,views.contact , name='contact'),
    path('products.html/' ,views.products , name='products'),
    path('products.html/single-product.html/' ,views.singleproduct , name='singleproduct'),
    path('login.html/' ,views.login , name='login'),
    path('nav.html/' ,views.navbar, name='nav'),
]