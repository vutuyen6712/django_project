from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
# from home.controllers import employeeController
from home.controllers.category import categoryController
from home.controllers.accounts import userController
from home.controllers.product import productController


urlpatterns = [
#shop 
    #index
    path('',views.index, name="Home"),
    path('men/productgrid',views.men_productgrid, name="men product"),
    path('men/productlist',views.men_productlist, name="men productlist"),
    path('men/details',views.men_details, name="men details"),
    path('women/productgrid',views.women_productgrid, name="women product"),
    path('women/productlist',views.women_productlist, name="women productlist"),
    path('contact',views.contact, name="contact"),
    
    #User Login
    path('user/login',views.UserLogin, name="user login"),
    path('user/user_login',userController.login,name='trang user_login'),

    #User Register
    path('user/register',views.UserRegister, name="user register"),
    path('user/create_register',userController.create,name='trang create_register'),

    #User Forget Password
    path('user/forget_password',views.UserForgetPassword, name="user forget password"),

    #User Change Password
    path('user/change_password',views.UserChangePassword, name="user change password"),

#admin  
    path('admin/',views.AdminIndex,name='page admin'),
 
    #page list category
  # path('admin/list_category',views.Admin_ListCategory,name='page list category'),
    path('admin/add_category',categoryController.create,name='page_add_category'),
    path('admin/list_category',categoryController.list,name='page_list_category'),
    path('admin/edit_category/<int:id>',categoryController.edit,name='page_list_category'),
    path('admin/update_category/<int:id>',categoryController.update,name='page_update_category'),
    path('admin/delete_category/<int:id>',categoryController.delete,name='page_deleta_category'),

    # Add Product
    path('admin/add_product',productController.create_product,name='page_add_product'),
    # path('admin/add_post_product',productController.create_product,name='page add post_product'),
    path('admin/list_product',productController.listproduct,name='page_list_product'),
    path('admin/edit_product/<int:id>',productController.edit_product,name='page_edit_product'),
    path('admin/delete_product/<int:id>',productController.delete_product,name='page_delete_product'),
    path('admin/update_product/<int:id>',productController.update_product,name='page_update_product'),


    # List User
    path('admin/list_user',userController.index,name='page list user'),
    
    # Contact
    path('admin/contact',views.Admin_Contact,name='page contact'),

    # order
    path('admin/order',views.Admin_Order,name='page order'),

    # List Order
    path('admin/list_order',views.Admin_ListOrder,name='page list order'),
    
    # Admin login
    path('admin/login',views.Admin_Login,name='page admin login'),

    # Admin register
    path('admin/register',views.Admin_Register,name='page admin register'),

    # Admin Forget Password
    path('admin/forget_password',views.Admin_ForgetPassword,name='page admin forget password'),

    # Admin Change Password
    path('admin/change_password',views.Admin_ChangePassword,name='page admin change password'),
    # ajax post
    path('admin/ajax_post',views.ajax_post,name='ajax post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
