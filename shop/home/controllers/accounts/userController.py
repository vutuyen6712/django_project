from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.contrib import auth


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from home.models import user
from home.libs.user import UserForm
from home.models import user_contacts
from home.libs.user_contact import UserContactFrom


# list user - page admin manager -
def index(request):
	list_user = user.objects.all()
	return render(request,'admin/shop/user/list_user.html',{'list_user':list_user})


#user register
def create(request):
	if request.method == "POST":
		list_user = user.objects.all()
		form = UserForm(request.POST)
		email = request.POST['email']
		password = request.POST['password'] 
		re_password = request.POST['re_password'] 
		for x in list_user:
			if x.email != email:
				if password == re_password:
					if form.is_valid():
						form.save()
						return redirect("/")
				form = UserForm() 
				return render(request,"home/shop/accounts/register.html",{'form':form})
			form = UserForm() 
			return render(request,"home/shop/accounts/register.html",{'form':form})

#user login
def login(request):
	check = 0;
	if request.method == "POST":
		list_user = user.objects.all()
		email = request.POST['email']
		password = request.POST['password'] 
		for x in list_user:
			if x.email == email and x.password == password:
				request.session['user'] = {
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

#user logout
def user_logout(request):
	if 'user' in request.session:
		del request.session['user']
		return redirect('/')

#edit user
def edit_user(request,id):
	edit_user = user.objects.get(id=id)
	list_user = user.objects.all()
	return render(request,"admin/shop/user/edit_user.html",{'edit_user':edit_user, 'list_user':list_user})

#update user
def update_user(request,id):
	User = user.objects.get(id=id)
	form = UserForm(request.POST,instance = User)
	if form.is_valid():
		form.save()
		return redirect("/admin/list_user")
	return render(request,"home/shop/user/edit_user.html",{'User':User})

#delete_user
def delete_user(request,id):
	User = user.objects.get(id=id)
	User.delete()
	return redirect("/admin/list_user")

#user contact
def contact(request):
	if request.method == "POST":
		form = UserContactFrom(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/")
	form = UserContactFrom()
	return render(request,"home/shop/contact.html",{'form':form})

#list contact_admin
def list_contact_admin(request):
	list_contact = user_contacts.objects.all()
	if 'admin' in request.session:
		return render(request,"admin/shop/user/contact.html",{'list_contact':list_contact})
	else:
		return redirect("/admin/")

#delete contact
def delete_contact(request,id):
	list_contact = user_contacts.objects.get(id=id)
	list_contact.delete()
	return redirect("/admin/contact")

#edit contact
def edit_contact(request,id):
	list_contact = user_contacts.objects.get(id=id)
	contact = user_contacts.objects.all()
	return render(request,"admin/shop/user/edit_contact.html",{'list_contact':list_contact, 'contact':contact})