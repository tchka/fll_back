from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.JobListView.as_view()),
    # path('register/', views.ProfileCreateAPIView.as_view())
]