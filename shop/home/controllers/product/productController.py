from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from home.models import Product
from home.models import Category
from home.libs.product import ProductFrom
from home.libs.category import CategoryFrom

# def index(request):
# 	cat = Category.objects.all()
# 	return render(request,"admin/shop/product/product.html",{'cat':cat}) 

# def create_product(request):
#     form = ProductFrom()
#     if request.method == "POST":
#         myfile = request.FILES['image']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)

#         request.POST = request.POST.copy()
#         request.POST['image'] = filename

#         form = ProductFrom(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("/admin/list_product")

#     return render(request,"admin/shop/product/add_product.html")
def create_product(request):
	cat = Category.objects.all().filter(parentID=0)
	if request.method == "POST":
		uploaded_file = request.FILES['image']
		fs = FileSystemStorage()
		name = fs.save(uploaded_file.name, uploaded_file)
		uploaded_file_url = fs.url(name)
		
		request.POST = request.POST.copy()
		request.POST['image'] = name
		form = ProductFrom(request.POST)
		
		if form.is_valid(): 
			form.save()
			return redirect("/admin/list_product")
	form = ProductFrom()
	return render(request,"admin/shop/product/add_product.html",{'form':form, 'cat':cat})

def listproduct(request):
	product = Product.objects.all()
	cat = Category.objects.all()
	return render(request,"admin/shop/product/list_product.html",{'product':product,'cat':cat })

def edit_product(request,id):
	product = Product.objects.get(id=id)
	cat = Category.objects.all().filter(parentID=0)
	return render(request,"admin/shop/product/edit_product.html",{'product': product, 'cat':cat})

def delete_product(request,id):
	product = Product.objects.get(id=id)
	product.delete()
	return redirect("/admin/list_product")

def update_product(request,id):
	product = Product.objects.get(id=id)
	form = ProductFrom(request.POST,instance = product)

	if request.method == "POST":
		uploaded_file = request.FILES['image']
		fs = FileSystemStorage()
		name = fs.save(uploaded_file.name, uploaded_file)
		uploaded_file_url = fs.url(name)
		
		request.POST = request.POST.copy()
		request.POST['image'] = name
		form = ProductFrom(request.POST)
		
		if form.is_valid(): 
			form.save()
			return redirect("/admin/list_product")
	form = ProductFrom()
	return render(request,"admin/shop/product/edit_product.html",{'product':product})

# list_cat_men
def list_cat_men(request):
	product_list = Product.objects.filter(cat_id=13)
	paginator  = Paginator(product_list,12)
	page = request.GET.get('page')
	try:
		product  = paginator.page(page) 
	except PageNotAnInteger:
		product  = paginator.page(1)
	except EmptyPage:
		product  = paginator.page(paginator.num_pages)
	# product = Product.objects.filter(cat_id=id)
	return render(request,"home/shop/men/productgrid.html",{'product':product})

	