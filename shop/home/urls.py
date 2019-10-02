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

    #category product
    path('men/productlist',productController.list_cat_men, name="men_productlist"),

    path('men/productgrid',productController.list_cat_men, name="men_product"),
    
    path('men/details',views.men_details, name="men details"),
    path('women/productgrid',views.women_productgrid, name="women_product"),
    path('women/productlist',views.women_productlist, name="women_productlist"),
    
    

    #User Login
    path('user/login',views.UserLogin, name="user login"),
    path('user/user_login',userController.login,name='user_login'),
    path('user/user_logout',userController.user_logout,name='user_logout'),

    #User Register
    path('user/register',views.UserRegister, name="user register"),
    path('user/create_register',userController.create,name='trang create_register'),

    #User Forget Password
    path('user/forget_password',views.UserForgetPassword, name="user_forget_password"),

    #User Change Password
    path('user/change_password',views.UserChangePassword, name="user_change_password"),

    #blog
    path('blog',views.blog, name="page_blog"),

    #User Contact
    path('contact',views.contact, name="contact"),
    path('user/contact',userController.contact, name="user_contact"),
#admin  
    path('admin/',views.AdminIndex,name='page admin'),
    # Admin login
    path('admin/login',views.admin_login,name='admin_login'),
    # Admin login
    path('admin/logout',views.admin_logout,name='admin_logout'),

    #page list category
    path('admin/add_category',categoryController.create,name='page_add_category'),
    path('admin/list_category',categoryController.list,name='page_list_category'),
    path('admin/edit_category/<int:id>',categoryController.edit,name='page_list_category'),
    path('admin/update_category/<int:id>',categoryController.update,name='page_update_category'),
    path('admin/delete_category/<int:id>',categoryController.delete,name='page_deleta_category'),

    # Add Product
    path('admin/add_product',productController.create_product,name='page_add_product'),
    path('admin/list_product',productController.listproduct,name='page_list_product'),
    path('admin/edit_product/<int:id>',productController.edit_product,name='page_edit_product'),
    path('admin/delete_product/<int:id>',productController.delete_product,name='page_delete_product'),
    path('admin/update_product/<int:id>',productController.update_product,name='page_update_product'),
    # ajax post
    path('admin/ajax_post',views.ajax_post,name='ajax post'),

    # List User
    path('admin/list_user',userController.index,name='page list user'),
    path('admin/edit_user/<int:id>',userController.edit_user,name='edit_user'),
    path('admin/update_user/<int:id>',userController.update_user,name='update_user'),
    path('admin/delete_user/<int:id>',userController.delete_user,name='update_user'),

    # Contact
    path('admin/contact',userController.list_contact_admin,name='list_contact'),
    path('admin/delete_contact/<int:id>',userController.delete_contact,name='delete_contact'),
    path('admin/edit_contact/<int:id>',userController.edit_contact,name='edit_contact'),
    # order
    path('admin/order',views.Admin_Order,name='page order'),

    # List Order
    path('admin/list_order',views.Admin_ListOrder,name='page list order'),
    
 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
