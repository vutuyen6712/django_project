from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from home.models import Category
from home.models import Product
from home.models import user
from home.models import admin
from django.db.models import Q

# Create your views here.
def index(request):
    cat = Category.objects.all().filter(parentID = 0)
    cat1 = Category.objects.all().filter(~Q(parentID = 0))
    # kids = Category.objects.all().filter(parentID=15)
    return render(request,"home/shop/index.html",{'cat':cat,'cat1':cat1})

#blog
def blog(request):
    cat = Category.objects.all().filter(parentID = 0)

    cat1 = Category.objects.all().filter(~Q(parentID = 0))
    return render(request,'home/shop/blog.html',{'cat':cat,'cat1':cat1})

def contact(request):
    cat = Category.objects.all().filter(parentID = 0)

    cat1 = Category.objects.all().filter(~Q(parentID = 0))
    return render(request,'home/shop/contact.html',{'cat':cat,'cat1':cat1})

# Login
def UserLogin(request):
	return render(request,"home/shop/accounts/login.html")
# register
def UserRegister(request):
	return render(request,"home/shop/accounts/register.html")

def UserForgetPassword(request):
    return render(request,'home/shop/accounts/forget_password.html')

def UserChangePassword(request):
    return render(request,'home/shop/accounts/change_password.html')

#admin
def AdminIndex(request):
	if 'admin' in request.session:
		return render(request,"admin/shop/index.html")
	else :
		return render(request,"admin/shop/accounts/login.html")


def Admin_AddProduct(request):
    return render(request,'admin/shop/product/add_product.html')

def Admin_ListProduct(request):
    return render(request,'admin/shop/product/list_product.html')

def Admin_Contact(request):
    return render(request,'admin/shop/user/contact.html')

def Admin_Order(request):
    return render(request,'admin/shop/order/order.html') 
 
def Admin_ListOrder(request):
    return render(request,'admin/shop/order/list_order.html')

# admin login
# Login
def admin_login(request):
	if request.method == "POST":
		email = request.POST['email']
		password = request.POST['password']
		list_admin = admin.objects.all()
		for x in list_admin:
			if email == x.email and password == x.password :
				request.session['admin'] = {
					'id':x.id,
					'email':x.email,
					'name':x.name,
				}
				break
	return redirect('/admin/')
#admin logout

def admin_logout(request):
	if 'admin' in request.session:
		del request.session['admin']
		return redirect('/admin/')


# ajax post
def ajax_post(request):
    if request.is_ajax():
        val = request.POST.get('val')
        cat_con = Category.objects.filter(parentID = val)
        template = loader.get_template('admin/layouts/demo.html')
        context = {
            'cat_con': cat_con,
        }
        return HttpResponse(template.render(context, request))
