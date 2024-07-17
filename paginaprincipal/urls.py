#from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from  . import views


urlpatterns = [
    path('', views.index, name='index'), 
    path('producto_1/', views.producto_1, name='producto_1'),
    path('producto_2/', views.producto_2, name='producto_2'),
    path('producto_3/', views.producto_3, name='producto_3'),
    path('producto_4/', views.producto_4, name='producto_4'),
    path('contacto/', views.contacto, name='contacto'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('carrito/', views.carrito, name='carrito'),

    
]


