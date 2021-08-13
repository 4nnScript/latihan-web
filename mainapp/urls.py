from django.urls import path
from . import views, api

urlpatterns = [
    path('count/<int:angka>/', views.count),
    path('sapa/<str:nama>/', views.sapa),
    path('shop/', views.shop),
    path('shop/laptop/', views.shop_laptop),
    path('shop/smartphone/', views.shop_smartphone),
    path('shop/console/', views.shop_console),
    path('shop/laptop/list/', views.laptop_list),
    path('buy/', views.buy),
    path('home/', views.home),
    path ('wedding/', views.wedding),
    path('firstpage/', views.first_page),
    path('secondpage/', views.second_page),
    path('example/', views.example),
    path('profile/', views.profile),
    path('second/', views.second_page),


    path('api/category/get-all/', api.get_categories),
    path('api/product/get-all/', api.get_products),
    path('api/category/create/', api.create_categories),
    path('', views.landing_page),
]
