from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_product, name='search_product'),
    path('add/', views.add_product, name='add_product'),
    path('update/<str:code>/', views.update_stock, name='update_stock'),
]
