from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from .serialisers import ProfileCreateSerializer
from .models import Profile

class ProfileCreateAPIView(CreateAPIView):
    model = Profile
    serializer_class = ProfileCreateSerializer

    def post(self, request, *args, **kwargs):
        data = {
            'fio': request.data.get('fio', None),
            'role': request.data.get('role', None),

        }

        serializer = ProfileCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)