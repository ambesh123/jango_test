from django.shortcuts import render
from django.http import HttpResponse
from isp.models import Isp

def index(request):
	qs = Isp.objects.all()
	return render(request,'index.html' , {'isp_list' : qs , 'tot_isp' : len(qs)})


def sortbyprice(request):
	res = "<table class = 'table'>"
	qs = Isp.objects.order_by('price')

	for i in qs :
	  res += "<tr class='success lisitem'><td><a name = '"+i.name+"'>"
	  res += i.name
	  res += "</a></td> <td id = 'alrt'>"
	  res += i.price
	  res += "</td></tr>"
	 
	res += "</table>"

	return HttpResponse(res)

def sortbyrating(request):
	res = "<table class = 'table'>"
	qs = Isp.objects.order_by('-rating')

	for i in qs :
	  res += "<tr class='success lisitem'><td><a name = '"+i.name+"'>"
	  res += i.name
	  res += "</a></td> <td id = 'alrt'>"
	  res += i.price
	  res += "</td></tr>"
	  
	res += "</table>"

	return HttpResponse(res)

def getDesc(request):
	nam = request.GET.get('name')

	qs = Isp.objects.filter(name = nam)

	res = "<h3> Max Speed : "
	res += str(qs[0].maxSpeed)
	res += "</h3><br>"
	res += "<div class = 'desc_detail'>"
	res += str(qs[0].desc)
	res += "</div>"
	res += "<h3> Rating :</h3><h1>"

	for i in range(qs[0].rating):
		res += "*"

	res += "</h1>"

	return HttpResponse(res)

