from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from home.models import Category
from home.models import Product
from home.models import user

# Create your views here.
def index(request):
    return render(request,"home/shop/index.html")

def men_productgrid(request):
    return render(request,'home/shop/men/productgrid.html')

def men_productlist(request):
    return render(request,'home/shop/men/productlist.html')

def men_details(request):
    return render(request,'home/shop/men/details.html')    

def women_productgrid(request):
    return render(request,'home/shop/women/productgrid.html')

def women_productlist(request):
    return render(request,'home/shop/women/productlist.html')

def contact(request):
    return render(request,'home/shop/contact.html')

# Login
def UserLogin(request):
	cat = Category.objects.all()
	return render(request,"home/shop/accounts/login.html",{
			'cat':cat
		}
	)
# register
def UserRegister(request):
	cat = Category.objects.all()
	return render(request,"home/shop/accounts/register.html",{
			'cat':cat
		}
	)

def UserForgetPassword(request):
    return render(request,'home/shop/accounts/forget_password.html')

def UserChangePassword(request):
    return render(request,'home/shop/accounts/change_password.html')

#admin
def AdminIndex(request):
    return render(request,'admin/shop/index.html')


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
def Admin_Login(request):
    return render(request,'admin/shop/accounts/login.html')

# admin register
def Admin_Register(request):
    return render(request,'admin/shop/accounts/register.html')

# admin forget password
def Admin_ForgetPassword(request):
    return render(request,'admin/shop/accounts/forget_password.html')

# admin change password
def Admin_ChangePassword(request):
    return render(request,'admin/shop/accounts/change_password.html')

# ajax post
def ajax_post(request ):
    if request.is_ajax():
        val = request.POST.get('val')
        cat_con = Category.objects.filter(parentID = val)
        template = loader.get_template('admin/layouts/demo.html')
        context = {
            'cat_con': cat_con,
        }
        return HttpResponse(template.render(context, request))
        # return redirect('page_add_product',value=cat_con)