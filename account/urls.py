from django.urls import path

from .views import ProfileUpdateView, ProfileRetrieveView, UserUpdateView, UserRetrieveView, UserListView

urlpatterns = [
    # path('signup/', register, name='signup'),
    # path('all', UserListView.as_view()),
    path('<int:pk>', UserRetrieveView.as_view()),
    path('update/<int:pk>', UserUpdateView.as_view()),
]
