from django.urls import path
from assignment import views

urlpatterns = [
    
    
    path('add/',views.form, name="a"),
    path('update/<int:id>/', views.stu_update, name="su"),
    path('',views.list_view, name= 'add'), 
    path('mark/<int:id>/',views.mark_view, name='mark') , 
    path('markadd/',views.add, name="ma"),
    path('markupdate/<int:id>/',views.mark_update, name='mu'),
    path('del/<int:id>/',views.delete, name="del"),
    path('delete/<int:id>/', views.dele, name="d"),
    path('json/<int:id>/', views.json, name = 'json'),
    path('con/', views.con, name='con'),
]

