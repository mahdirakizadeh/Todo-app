from django.urls import path
from . import views

urlpatterns = [

    path('', views.Home, name='home'),
    path('detail/<int:todo_id>/', views.Detail, name='details'),
    path('delete/<int:todo_id>/', views.Delete, name='delete'),
    path('create/', views.Create, name='create'),
    path('update/<int:todo_id>/', views.Update, name='update'),

]
