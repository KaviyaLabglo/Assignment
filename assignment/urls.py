from django.urls import path
from assignment import views

urlpatterns = [
    
   
    path('list/',views.list_view, name= 'list'),
    
    path('add/',views.form, name="a"),
    path('delete/<int:id>/', views.dele, name="d"),
    path('update/<int:id>/', views.stu_update, name="su"),
     
    path('mark/<int:id>/',views.mark_view, name='mark') , 
    
    path('markadd/',views.add, name="ma"),
    path('markupdate/<int:id>/',views.mark_update, name='mu'),
    path('del/<int:id>/',views.delete, name="del"),
   
    path('json/<int:id>/', views.json, name = 'json'),
    path('con/', views.con, name='con'),
    
    path('logout/',views.logout_user, name='logout'),
]

