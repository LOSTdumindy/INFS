from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Core features
    path('', include('core.urls')),

    # Auth routes
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # App-specific routes
    path('menu/', include('menu.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('orders.urls')),
    path('qr/', include('qrcodes.urls')),
    path('users/', include('users.urls')), 
    path('accounts/login/', auth_views.LoginView.as_view()),
     path('login/', auth_views.LoginView.as_view(template_name='your_app/custom_login.html'), name='login'),

]
