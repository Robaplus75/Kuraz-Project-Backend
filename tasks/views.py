from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer, TaskCompletedSerializer

class TaskListCreateAPIView(generics.ListCreateAPIView):
	''' View for listing and creating tasks'''

	queryset = Task.objects.all().order_by('-created_at')
	serializer_class = TaskSerializer

class TaskUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCompletedSerializer
