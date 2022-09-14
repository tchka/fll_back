from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .models import Category, ExecutorLevel, OrderStatus, Order, Message, Ticket, Review
from django.contrib.auth.models import User
from .serializers import CategorySerializer, CategoryCreateSerializer, ExecutorLevelSerializer, \
    ExecutorLevelCreateSerializer, OrderStatusSerializer, OrderStatusCreateSerializer, OrderSerializer, \
    OrderCreateSerializer, OrderUnpublishedSerializer, OrderPublishSerializer, MessageSerializer, \
    MessageCreateSerializer, TicketSerializer, TicketCreateSerializer, ReviewSerializer, ReviewCreateSerializer


class CategoryRetrieveView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdateView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer
    # permission_class = permissions.IsAuthenticatedOrReadOnly


class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer
    # permission_class = permissions.IsAuthenticatedOrReadOnly


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ExecutorLevelRetrieveView(generics.RetrieveAPIView):
    queryset = ExecutorLevel.objects.all()
    serializer_class = ExecutorLevelSerializer


class ExecutorLevelUpdateView(generics.UpdateAPIView):
    queryset = ExecutorLevel.objects.all()
    serializer_class = ExecutorLevelCreateSerializer
    # permission_class = permissions.IsAuthenticatedOrReadOnly


class ExecutorLevelCreateView(generics.CreateAPIView):
    queryset = ExecutorLevel.objects.all()
    serializer_class = ExecutorLevelCreateSerializer
    # permission_class = permissions.IsAuthenticatedOrReadOnly


class ExecutorLevelListView(generics.ListAPIView):
    queryset = ExecutorLevel.objects.all()
    serializer_class = ExecutorLevelSerializer


class OrderStatusRetrieveView(generics.RetrieveAPIView):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer


class OrderStatusUpdateView(generics.UpdateAPIView):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusCreateSerializer
    # permission_class = permissions.IsAuthenticatedOrReadOnly


class OrderStatusCreateView(generics.CreateAPIView):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusCreateSerializer
    # permission_class = permissions.IsAuthenticatedOrReadOnly


class OrderStatusListView(generics.ListAPIView):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer


class MessageRetrieveView(generics.RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageUpdateView(generics.UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageCreateSerializer
    # permission_class = permissions.IsAuthenticatedOrReadOnly


class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageCreateSerializer
    # permission_class = permissions.IsAuthenticatedOrReadOnly


class MessageListView(generics.CreateAPIView):
    # queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        queryset = Message.objects.all()

        params = self.request.query_params

        executor = params.get('executor', None)
        customer = params.get('customer', None)
        from_date = params.get('from_date', None)
        to_date = params.get('to_date', None)

        if executor:
            queryset = queryset.filter(executor__id=executor)

        if customer:
            queryset = queryset.filter(customer__id=customer)

        if from_date:
            queryset = queryset.filter(create_time__gte=from_date)

        if to_date:
            queryset = queryset.filter(create_timee__lte=to_date)

        return queryset


class TicketRetrieveView(generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketUpdateView(generics.UpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketCreateSerializer
    # permission_class = permissions.IsAuthenticatedOrReadOnly


class TicketCreateView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketCreateSerializer
    # permission_class = permissions.IsAuthenticatedOrReadOnly


class TicketListView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class ReviewRetrieveView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewUpdateView(generics.UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer
    # permission_class = permissions.IsAuthenticatedOrReadOnly


class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer
    # permission_class = permissions.IsAuthenticatedOrReadOnly


class ReviewListView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class OrderRetrieveView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_class = permissions.IsAuthenticatedOrReadOnly


class OrderUnpublishedUpdateView(generics.UpdateAPIView):
    serializer_class = OrderUnpublishedSerializer

    # permission_class = permissions.IsAuthenticatedOrReadOnly
    def get_queryset(self):
        return Order.objects.filter(status__id=1)


class OrderPublishUpdateView(generics.UpdateAPIView):
    serializer_class = OrderPublishSerializer

    # permission_class = permissions.IsAuthenticatedOrReadOnly
    def get_queryset(self):
        return Order.objects.filter(status__id=1)

    def partial_update(self, request, *args, **kwargs):
        order = self.get_object()

        order.status = 2
        order.save()
        serializer = OrderPublishSerializer(order, partial=True)
        return Response(serializer.data)


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    # permission_class = permissions.IsAuthenticatedOrReadOnly


class OrderListView(generics.ListAPIView):
    # queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = Order.objects.all()
        params = self.request.query_params

        customer = params.get('customer', None)
        executor = params.get('executor', None)
        status = params.get('status', None)
        type = params.get('type', None)

        if customer:
            queryset = queryset.filter(customer__id=customer)
        if executor:
            queryset = queryset.filter(executor__id=executor)
        if type:
            queryset = queryset.filter(type=type)
        if status:
            queryset = queryset.filter(status=status)

        return queryset


class OrderPublishedListView(generics.ListAPIView):
    queryset = Order.objects.filter(status_id=2)
    serializer_class = OrderSerializer
