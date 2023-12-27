from django.urls import path 
from . import views 
app_name = 'newapp'
urlpatterns = [ 
    path('home/', views.form_view), 
    
] 