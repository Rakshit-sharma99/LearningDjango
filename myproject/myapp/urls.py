from django.urls import path, re_path
from . import views

urlpatterns = [
    # Template route
    path('mytemplate/', views.mytemplate, name='mytemplate'),

    # Divide by zero route to test custom 500 error
    path('dv/', views.dv, name='dv'),

    # Application routes
    path('studentdetails/', views.studentdetails, name='studentdetails'),
    path('std/', views.std, name='std'),
    path('std1/', views.std1, name='std1'),
    path('std2/', views.std2, name='std2'),
    path('food/<str:food_value>/', views.fooddie, name='fooddie'),
    path('mart/', views.mart, name='mart'),
    path('calculator/', views.calculator, name='calculator'),

    # Regular expression routes
    re_path(r'^customer/(?P<customer_id>\d+)/$', views.customer, name='customer'),
    re_path(r'^dob/(?P<dob>\d{4}-\d{2}-\d{2})/$', views.dob, name='dob'),
    re_path(r'^menu/(?P<category>[\w -]+)/(?:(?P<subcat>[\w -]*)/)?$', views.menu, name='menu'),
]