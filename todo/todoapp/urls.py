
from django.urls import path
# from todoapp.views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView
from todoapp import views

urlpatterns =[
    path('display/',views.DisplayAllTask,name='display'),
    path('',views.AddTasks,name='add'),
    # path('edit/<int:pk>/',views.EditTask,name='edit'),
    path('edit/<int:id>/',views.EditTask,name='edit'),
    path('delete/<int:id>/',views.DeleteTask,name='delete'),
    # path('<int:id>/',views.paginatorPage),
   
    
]
