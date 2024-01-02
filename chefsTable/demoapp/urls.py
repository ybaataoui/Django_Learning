from django.urls import path 
from . import views 
app_name = 'demoapp'
urlpatterns = [ 
    # path('home/', views.form_view),
    path('home/', views.home, name='home'), 
    path('about/', views.about, name="about"), 
    path('menu/', views.menu, name="menu"),
    path('book/', views.book, name="book"), 
     
    # path('getuser/', views.qryview, name='qryview'), 
    # path('showform/', views.showform, name='showform'),
    # path('getform/', views.getform, name='getform'),
    # path('dishes/<str:dish>', views.menuitems, name='menuitems'),
    # path('login/', views.loginform, name='login'),
    
] 