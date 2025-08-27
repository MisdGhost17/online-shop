"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from products.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('users/', include('users.urls')),


    path('api/v1/product/', ProductViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/product/<int:pk>/', ProductViewSet.as_view({'get': 'product_detail', 'delete': 'destroy', 'put': 'update'})),

    path('api/v1/char/', ProductCharacteristicsViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/char/<int:pk>/', ProductCharacteristicsViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'})),
    path('api/v1/productchars/<int:pk>/', ProductCharacteristicsViewSet.as_view({'get': 'get_chars', 'post': 'create'})),

    path('api/v1/category/', ProductCategoryViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/category/<int:pk>/', ProductCategoryViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'})),

    path('api/v1/productimages/', ProductImagesViewSet.as_view({'get': 'list', 'post': 'create'})),

    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'api/v1/auth/', include('djoser.urls.authtoken')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)