from django.shortcuts import render , redirect
from django.http import HttpResponse

import datetime

# Create your views here.

def index(request):
	return HttpResponse("<h1>Django Server is online!<br> Enjoy!!</h1>")

def check(request):
   return render(request,'check.html')

def check2(request):
	time = datetime.datetime.now()
	n = 100
	lst = [0]*n
	for i in range(n) :
		lst[i] = i+1
	return render(request,'check2.html' , {"time" : time , "list" : lst})


def viewArticle(request , articleID):
   text = "Displaying article Number : %s" %articleID
   return HttpResponse(text)