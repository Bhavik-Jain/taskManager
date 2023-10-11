from . import views
from django.urls import path


urlpatterns = [
	path('view_tasks/', views.view_tasks, name="view_tasks"),
	path('create_task/', views.create_task, name="create_task"),
	path('update_task/<str:id>/', views.update_task, name="update_task"),
	path('delete_task/<str:id>/', views.delete_task, name="delete_task"),
]