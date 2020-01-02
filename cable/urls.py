
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasklist', views.taskList, name='task-list'),
    #path('task/<int:id>', views.taskView, name='task-view'),
    path('newtask/', views.newTask, name='new-task'),
    #path('edittask/<int:id>', views.editTask, name='edit-task'),
    #path('deletetask/<int:id>', views.deleteTask, name='delete-task'),
    #path('changestatus/<int:id>', views.changeStatus, name='change-status'),
    #path('fatura/', views.faturaTask, name='fatura-task'),
    path('helloworld/', views.helloworld),

]