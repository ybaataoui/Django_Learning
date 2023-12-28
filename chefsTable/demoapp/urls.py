from django.urls import path 
from . import views 
app_name = 'demoapp'
urlpatterns = [ 
    path('home/', views.form_view), 
    path('about/', views.about), 
    path('menu_card/', views.menu_by_id), 
    # path('home', views.home, name='home'), 
    # path('getuser/', views.qryview, name='qryview'), 
    # path('showform/', views.showform, name='showform'),
    # path('getform/', views.getform, name='getform'),
    # path('dishes/<str:dish>', views.menuitems, name='menuitems'),
    # path('login/', views.loginform, name='login'),
    
] 