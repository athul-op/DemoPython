from . import views
from django.urls import path




urlpatterns = [
    path('place_order/',views.place_orders,name='place_order'),
    # path('<int:pk>/', views.person_update_view, name='person_change'),
    path('ajax_load_course/', views.load_course, name='ajax_load_course'),
      
]