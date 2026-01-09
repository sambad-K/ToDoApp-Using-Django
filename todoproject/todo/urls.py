from django.urls import path,include  
from .views import task_list,task_created,task_updated
urlpatterns=[
    path('',task_list,name='task_list'),
    path('add/',task_created,name="task_created"),
    path('edit/<int:pk>/',task_updated,name='task_updated'),
]