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
    	view = views()
	return render(request,'contact.html')

def bloghome(request):
	view = views()
	return render(request,'blog-home.html')

def blogsingle(request):
    	view = views()
	return render(request,'blog-single.html')

def elements(request):
    	view = views()
	return render(request,'elements.html')

def portfolio(request):
    	view = views()
	return render(request,'portfolio.html')

def price(request):
    	view = views()
	return render(request,'price.html')

def services(request):
    	view = views()
	return render(request,'services.html')