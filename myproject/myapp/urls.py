"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentdetails/', views.studentdetails, name='studentdetails'),
    path('std/', views.std, name='std'),
    path('std1/', views.std1, name='std1'),
    path('std2/', views.std2, name='std2'),
    path('food/<str:food_value>/', views.fooddie, name='fooddie'),
    path('mart/', views.mart, name='mart'),
    path('calculator/', views.calculator, name='calculator'),
# regular expresssion  + used for 1 or more characters
    # re_path(r'^customer/(?P<customer_id>[a-zA-Z]+)/$', views.customer),
            

            # * used for 0 or more characters

    # \d used for digits
    re_path(r'^customer/(?P<customer_id>\d+)/$', views.customer),

    #specific number of digits

        re_path(r'^dob/(?P<dob>\d{4}-\d{2}-\d{2})/$', views.dob),
]

