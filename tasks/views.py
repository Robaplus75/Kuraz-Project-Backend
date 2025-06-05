from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer, TaskCompletedSerializer

class TaskListCreateAPIView(generics.ListCreateAPIView):
	''' View for listing and creating tasks'''

	queryset = Task.objects.all().order_by('-created_at')
	serializer_class = TaskSerializer

class TaskUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
	''' view for updating task completion and deleting a task'''
	queryset = Task.objects.all()
	serializer_class = TaskCompletedSerializer

class TaskFilterAPIView(generics.ListAPIView):
	'''View for filtering tasks by completion'''
	serializer_class = TaskSerializer

	def get_queryset(self):
		queryset = Task.objects.all()
		completed = self.request.query_params.get('completed')

		if completed is not None:
			completed = completed.lower() == 'true'
			queryset = queryset.filter(completed=completed)

		return queryset