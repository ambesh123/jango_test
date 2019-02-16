from django.shortcuts import render
from django.http import HttpResponse
from login.models import Users

def index(request):
	return render(request,'form.html')

def signin(request):
	uname = str(request.POST.get('username'))
	pwd = str(request.POST.get('password'))
	qs = Users.objects.all()
	valid = False
	for i in qs:
		if i.uname == uname and i.pwd == pwd:
			request.session.__setitem__('uname' , uname)
			valid = True

	if not valid :
		return HttpResponse("Wrong Username or Password")
		
	return HttpResponse("Welcome " + str(request.session.__getitem__('uname')))