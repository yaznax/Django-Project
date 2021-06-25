from django.shortcuts import render
from .models import *

# Create your views here.
def views():
    view = {}
	view['feedback'] = Feedback.objects.all()

    	
def home(request):
	view = views()
	return render(request,'index.html',view)

def about(request):
    view = views()
	return render(request,'about.html',view)

def contact(request):
	return render(request,'contact.html')

def bloghome(request):
	return render(request,'blog-home.html')

def blogsingle(request):
	return render(request,'blog-single.html')

def elements(request):
	return render(request,'elements.html')

def portfolio(request):
	return render(request,'portfolio.html')

def price(request):
	return render(request,'price.html')

def services(request):
	return render(request,'services.html')