from django.urls import path, include
from .views import *
urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('projects/', ProjectList.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetail.as_view(), name='project-detail'),
    path('projects/<int:project_id>/boards/', BoardList.as_view(), name='board-list'),
    path('projects/<int:project_id>/boards/<int:pk>/', BoardDetail.as_view(), name='board-detail'),
    path('projects/<int:project_id>/boards/<int:board_id>/tasks/', TaskList.as_view(), name='task-list'),
    path('projects/<int:project_id>/boards/<int:board_id>/tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('boards/', BoardListAll.as_view(), name='list-all-boards'),
    path('tasks/', TaskListAll.as_view(), name='list-all-tasks'),
]