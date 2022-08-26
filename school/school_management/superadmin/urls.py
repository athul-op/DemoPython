from django.urls import path
from . import views

urlpatterns = [
    path('',views.master_signin,name="admin_signin"),
    path('admin_home/',views.admin_home,name="admin_home"),
    path('customer/',views.customer,name="customer"),
    path('customer_pickoff/<customer_id>',views.customer_pickoff,name="customer_pickoff"),
    path('add_department/',views.add_department,name="add_department"),
    path('add_course/',views.add_course,name="add_course"),
    path('add_material/',views.add_Material,name="add_material"),
    path('order_details',views.order_details,name='order_details'),
    path('admin_logout',views.admin_logouts,name='admin_logout'),
] 