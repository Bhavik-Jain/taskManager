from rest_framework import serializers
from .models import TasksStore

class TasksSerializer(serializers.ModelSerializer):
	class Meta:
		model = TasksStore
		fields ='__all__'