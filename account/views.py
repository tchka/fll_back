from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from .serialisers import UserSerializer, ProfileSerializer, UserRetrieveSerializer, UserUpdateSerializer
from .models import Profile
from django.contrib.auth import get_user_model
from .permissions import IsOwner


#
# class ProfileCreateView(generics.CreateAPIView):
#     model = Profile
#     serializer_class = ProfileCreateSerializer
#
#     def post(self, request, *args, **kwargs):
#         data = {
#             'fio': request.data.get('fio', None),
#             'email': request.data.get('email', None),
#             'role': request.data.get('role', None),
#         }
#
#         serializer = ProfileCreateSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileRetrieveView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileUpdateView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserRetrieveView(generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserRetrieveSerializer
    permission_class = IsOwner


class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserUpdateSerializer
    permission_class = IsOwner


class UserListView(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserRetrieveSerializer
