from rest_framework import serializers

from .models import Job

class JobListSerializer(serializers.ModelSerializer):
    """ Список заявок """

    class Meta:
        model = Job
        fields = ('name', 'description', 'length', 'execution_time', 'create_time')
