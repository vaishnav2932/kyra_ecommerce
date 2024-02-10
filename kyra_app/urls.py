from django.urls import path
from kyra_app import views

urlpatterns=[

    path('',views.home.as_view(),name="home"),
    path('register/',views.registerview.as_view(),name="register"),
    path('login/',views.loginview.as_view(),name=" login"),
    path('products/<int:pk>',views.productsview.as_view(),name="products")
]
