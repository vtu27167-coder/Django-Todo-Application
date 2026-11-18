
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('addTask/', views.addTask, name='addTask'),

    path('completeTask/<int:task_id>/', views.complete, name='complete'),

    path('incompleteTask/<int:task_id>/', views.incomplete, name='incomplete'),

    path('updateTask/<int:task_id>/', views.updateData, name='updateData'),

    path('deleteTask/<int:task_id>/', views.deleteTask, name='deleteTask'),
]
