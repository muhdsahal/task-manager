from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from accounts.views import IsAdminOrSuperAdmin,IsSuperAdmin,IsOwnerOrAdmin,CustomIsAuthenticated

class TaskListAPI(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [CustomIsAuthenticated]
    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user)

class TaskUpdateAPI(generics.RetrieveUpdateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [CustomIsAuthenticated,IsOwnerOrAdmin]
    lookup_url_kwarg = 'id'
    queryset = Task.objects.all()

class TaskReportAPI(generics.RetrieveAPIView):
    serializer_class = TaskSerializer
    permission_classes = [CustomIsAuthenticated,IsAdminOrSuperAdmin]
    lookup_url_kwarg = 'id'
    queryset = Task.objects.filter(status=Task.STATUS_COMPLETED)
