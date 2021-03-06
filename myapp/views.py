from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Person , Photo
from django.conf import settings
from django.core.files.storage import FileSystemStorage

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

def passName(request):
	return render(request,'passname.html')

def nextPage(request):
	nam = request.GET.get('nam','Anonymous')
	return render(request,'nextpage.html',{'nam':nam})

def getPersons(request):
	res = "<table>"
	qs = Person.objects.all()
	for i in range(len(qs)):
		res += "<tr><th>"+qs[i].name+"</th><td>"+qs[i].mobile+"</td></tr>"
	res += "</table>"
	return HttpResponse(res)

def checkUpload(request):
	return render(request,'checkupload.html')

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'checkupload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'checkupload.html')
