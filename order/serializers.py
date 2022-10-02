from rest_framework import serializers

from .models import Category, ExecutorLevel, OrderStatus, Order, Message, Ticket, Review
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from account.serialisers import UserSerializer, UserRetrieveSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ExecutorLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecutorLevel
        fields = '__all__'


class ExecutorLevelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecutorLevel
        fields = '__all__'


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = '__all__'


class OrderStatusCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    # type = serializers.CharField(source='get_type_display')
    executor_level = serializers.SlugRelatedField(queryset=ExecutorLevel.objects.all(), slug_field='name')
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')
    status = serializers.SlugRelatedField(queryset=OrderStatus.objects.all(), slug_field='name')
    customer = serializers.SlugRelatedField(queryset=get_user_model().objects.all(), slug_field='username')
    executor = serializers.SlugRelatedField(queryset=get_user_model().objects.all(), slug_field='username')

    class Meta:
        model = Order
        # fields = '__all__'
        fields = (
            'id', 'name', 'category', 'description', 'keyword', 'length', 'price', 'customer', 'executor_level',
            'execution_time', 'executor', 'status')
        read_only_fields = ('id', 'customer',)

class OrderWorkoutSerializer(serializers.ModelSerializer):
    # type = serializers.CharField(source='get_type_display')
    executor_level = serializers.SlugRelatedField(queryset=ExecutorLevel.objects.all(), slug_field='name')
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')
    status = serializers.SlugRelatedField(queryset=OrderStatus.objects.all(), slug_field='name')
    customer = serializers.SlugRelatedField(queryset=get_user_model().objects.all(), slug_field='username')
    executor = serializers.SlugRelatedField(queryset=get_user_model().objects.all(), slug_field='username')

    class Meta:
        model = Order
        # fields = '__all__'
        fields = (
            'id', 'name', 'category', 'description', 'keyword', 'length', 'price', 'customer', 'executor_level',
            'execution_time', 'executor', 'status', 'article')
        read_only_fields = ('id', 'name', 'category', 'description', 'keyword', 'length', 'price', 'customer', 'executor_level',
            'execution_time', 'executor')


class OrderUnpublishedSerializer(serializers.ModelSerializer):
    # type = serializers.CharField(source='get_type_display')
    executor_level = serializers.SlugRelatedField(queryset=ExecutorLevel.objects.all(), slug_field='name')
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')
    status = serializers.SlugRelatedField(queryset=OrderStatus.objects.all(), slug_field='name')

    class Meta:
        model = Order
        # fields = '__all__'
        fields = (
            'id', 'name', 'category', 'description', 'keyword', 'length', 'price', 'executor_level', 'execution_time',
            'status')
        read_only_fields = ('id', 'status',)


class OrderStatusByCustomerSerializer(serializers.ModelSerializer):
    status = serializers.SlugRelatedField(queryset=OrderStatus.objects.all(), slug_field='name')

    class Meta:
        model = Order
        # fields = '__all__'
        fields = (
            'id', 'name', 'status',)
        read_only_fields = ('id', 'name',)


class OrderStatusByExecutorSerializer(serializers.ModelSerializer):
    status = serializers.SlugRelatedField(queryset=OrderStatus.objects.all(), slug_field='name')
    executor = UserSerializer()

    class Meta:
        model = Order
        # fields = '__all__'
        fields = (
            'id', 'name', 'status', 'executor',)
        read_only_fields = ('id', 'name',)


class OrderCreateSerializer(serializers.ModelSerializer):
    # type = serializers.CharField(source='get_type_display')
    executor_level = serializers.SlugRelatedField(queryset=ExecutorLevel.objects.all(), slug_field='name')
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')

    class Meta:
        model = Order
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    recipient = UserSerializer()

    class Meta:
        model = Message
        fields = '__all__'


class MessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    severity = serializers.CharField(source='get_severity_display')

    class Meta:
        model = Ticket
        fields = '__all__'


class TicketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    recipient = UserSerializer()

    class Meta:
        model = Review
        fields = '__all__'


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
