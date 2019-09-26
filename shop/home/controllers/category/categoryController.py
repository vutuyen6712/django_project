from django.shortcuts import render,redirect
from django.http import HttpResponse

from home.models import Category
from home.libs.category import CategoryFrom

def create(request):
	if request.method == "POST":
		form = CategoryFrom(request.POST)
		if form.is_valid(): 
			form.save()
			return redirect("/admin/list_category")
	form = CategoryFrom()
	return render(request,"admin/shop/category/list_category.html",{'form':form})

def list(request):
	category = Category.objects.all()
	return render(request,"admin/shop/category/list_category.html",{'category':category})

def delete(request,id):
	category = Category.objects.get(cat_id=id)
	category.delete()
	return redirect("/admin/list_category")

def edit(request,id):
	category = Category.objects.get(cat_id=id)
	cat = Category.objects.all()
	return render(request,"admin/shop/category/edit_category.html",{'category':category, 'cat':cat})

def update(request,id):
	category = Category.objects.get(cat_id=id)
	form = CategoryFrom(request.POST,instance = category)
	if form.is_valid():
		form.save()
		return redirect("/admin/list_category")
	return render(request,"home/shop/category/edit_category.html",{'category':category})