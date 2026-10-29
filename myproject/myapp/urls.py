from django.urls import path, re_path
from . import views

urlpatterns = [
    # Template route
#     path('mytemplate/', views.mytemplate, name='mytemplate'),
#     # re_path(r'^fooddata/(?P<fooddata>[\w -]+)/?:(?P<item_name>[\w -]*)/)?$', views.fooddata, name='fooddata'),
# # re_path(r'^fooddata/(?P<item_name>[\w -]+)/$', views.fooddata, name='fooddata'),
# #    path('fooddata/<str:item_name>/', views.fooddata, name='fooddata'),
#     # Divide by zero route to test custom 500 error
#     path('dv/', views.dv, name='dv'),
#     path ('testimage/', views.testimage, name='testimage'),
#     path ('events/', views.events, name='events'),
#     # Fixed: ' eventbooking' se leading space hataya taaki {% url 'eventbooking' %} theek se chale
#     path('booking/', views.eventbooking, name='eventbooking'),
#     path('eventbook/<str:eventdetails>/', views.eventbook, name='eventbook'),
#     # Application routes
#     path('studentdetails/', views.studentdetails, name='studentdetails'),
#     path('std/', views.std, name='std'),
#     path('std1/', views.std1, name='std1'),
#     path('std2/', views.std2, name='std2'),
#     path('food/<str:food_value>/', views.fooddie, name='fooddie'),
#     path('mart/', views.mart, name='mart'),
#     path('calculator/', views.calculator, name='calculator'),\
#     path('temp/', views.temp, name='temp'),
   
#     # Regular expression routes
#     re_path(r'^customer/(?P<customer_id>\d+)/$', views.customer, name='customer'),
#     re_path(r'^dob/(?P<dob>\d{4}-\d{2}-\d{2})/$', views.dob, name='dob'),
#     re_path(r'^menu/(?P<category>[\w -]+)/(?:(?P<subcat>[\w -]*)/)?$', views.menu, name='menu'),
#     # re_path(r'^fooddata/(?P<fooddata>[\w -]+)/?:(?P<item_name>[\w -]*)/)?$', views.fooddata, name='fooddata'),
#     path('csstest/', views.csstest, name='csstest'),
#     path('plan/', views.plan, name='plan'),
#     path('phones/',views.phones, name='phone'),
#     path('umar/',views.umar, name='umar'),
#     path('base/',views.base),
#     path('home/',views.home),
#     path('about/',views.about),
#     path ('greet/<str:name>/<str:time>',views.greet),
#     path('dish/<str:food>',views.dishes),
#     path('calc/',views.calc),
#     path('depart/',views.departments),
#     path('depdet/<str:department_name>/',views.department_details),











    path('students/',views.student_result),
    path('stdetails/<int:rno>/',views.stdeatils),
    path('student/', views.student),
    path('htmlform/', views.htmlform, name='htmlform'),

    path('validate/', views.validate, name='validate'),
    path('inputform1/', views.form_submission, name='inputform1'),
    path('inputform2/', views.form_submission, name='inputform1'),
        ]
    


