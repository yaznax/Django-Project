from django.urls import path
from .views import *
app_name="home"
urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('bloghome', bloghome, name='bloghome'),
    path('blogsingle', blogsingle, name='blogsingle'),
    path('elements', elements, name='elements'),
    path('portfolio', portfolio, name='portfolio'),
    path('price', price, name='price'),
    path('services', services, name='services'),
    

]
