from django.urls import path
from .views import TaskListAPI, TaskUpdateAPI, TaskReportAPI

urlpatterns = [
    path('tasks/', TaskListAPI.as_view(), name='task-list'),
    path('tasks/<int:id>/', TaskUpdateAPI.as_view(), name='task-update'),
    path('tasks/<int:id>/report/', TaskReportAPI.as_view(), name='task-report'),
]
