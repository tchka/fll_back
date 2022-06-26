from rest_framework.response import Response

from rest_framework.views import APIView

from .models import Job
from .serializers import JobListSerializer

class JobListView(APIView):
    """Вывод списка заявок"""

    def get(self, request):
        jobs = Job.objects.all()
        serializer = JobListSerializer(jobs, many=True)
        return Response(serializer.data)