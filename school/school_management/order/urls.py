from . import views
from django.urls import path




urlpatterns = [
    path('place_order/',views.place_orders,name='place_order'),
      
]