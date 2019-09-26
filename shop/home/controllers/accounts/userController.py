from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
	
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from home.models import user
from home.libs.user import UserForm


# list user - page admin manager -
def index(request):
	list_user = user.objects.all()
	return render(request,'admin/shop/user/list_user.html',{'list_user':list_user})

def create(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		password = request.POST['password'] 
		re_password = request.POST['re_password'] 
		if password == re_password:
			if form.is_valid():
				form.save()
				return redirect("/")
		form = UserForm() 
		return render(request,"home/shop/accounts/register.html",{'form':form})

def login(request):
	check = 0;
	if request.method == "POST":
		list_user = user.objects.all()
		email = request.POST['email']
		password = request.POST['password'] 
		for x in list_user:
			if x.email == email and x.password == password:
				request.session['login'] = {
					'id':x.id,
					'name':x.name
				}
				check = 1
				break;
		if check == 1:
			return redirect("/")
		elif check == 0:
			form = UserForm()
			return render(request,"home/shop/accounts/login.html",{'form':form})

def contact(request):
	if request.method == "POST":
		form = User_contactsFrom(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/")
	form = User_contactsFrom()
	return render(request,"home/shop/contact.html",{'form':form})

def list_contact_admin(request):
	list_contact = user_contacts.objects.all()
	return render(request,"admin/shop/contact.html",{'list_contact':list_contact})

 