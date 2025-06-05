from rest_framework.serializers import ModelSerializer
from .models import Task

class TaskSerializer(ModelSerializer):
	""" Serializer for the Task Model """
	class Meta:
		model = Task
		fields = ['id', 'title', 'description', 'completed', 'dead_line', 'created_at', 'updated_at']

class TaskCompletedSerializer(ModelSerializer):
	""" Serializer for completeing a task """
	class Meta:
		model = Task
		fields = ['completed']