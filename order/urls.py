from django.urls import path
from . import views

urlpatterns = [
    # path('category/<int:pk>', views.CategoryRetrieveView.as_view()),
    # path('category/update/<int:pk>', views.CategoryUpdateView.as_view()),
    # path('category/all', views.CategoryListView.as_view()),
    # path('category/new', views.CategoryCreateView.as_view()),
    # path('executor-level/<int:pk>', views.ExecutorLevelRetrieveView.as_view()),
    # path('executor-level/update/<int:pk>', views.ExecutorLevelUpdateView.as_view()),
    # path('executor-level/all', views.ExecutorLevelListView.as_view()),
    # path('executor-level/new', views.ExecutorLevelCreateView.as_view()),
    # path('order-status/<int:pk>', views.CategoryRetrieveView.as_view()),
    # path('order-status/update/<int:pk>', views.OrderStatusUpdateView.as_view()),
    path('order-status/all', views.OrderStatusListView.as_view()),
    # path('order-status/new', views.OrderStatusCreateView.as_view()),
    path('message/<int:pk>', views.MessageRetrieveView.as_view()),
    path('message/update/<int:pk>', views.MessageUpdateView.as_view()),
    path('message/all', views.MessageListView.as_view()),
    path('message/new', views.MessageCreateView.as_view()),
    path('ticket/<int:pk>', views.TicketRetrieveView.as_view()),
    path('ticket/update/<int:pk>', views.TicketUpdateView.as_view()),
    path('ticket/all', views.TicketListView.as_view()),
    path('ticket/new', views.TicketCreateView.as_view()),
    path('review/<int:pk>', views.ReviewRetrieveView.as_view()),
    path('review/update/<int:pk>', views.ReviewUpdateView.as_view()),
    path('review/all', views.ReviewListView.as_view()),
    path('review/new', views.ReviewCreateView.as_view()),
    path('order/<int:pk>', views.OrderRetrieveView.as_view()),
    path('order/update/<int:pk>', views.OrderUpdateView.as_view()),
    path('order/all', views.OrderListView.as_view()),
    path('order/published', views.OrderPublishedListView.as_view()),
    path('order/new', views.OrderCreateView.as_view()),
]
