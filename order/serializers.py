from rest_framework import serializers

from .models import Category, ExecutorLevel, OrderStatus, Order, Message, Ticket, Review
from django.contrib.auth.models import User

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
    type = serializers.CharField(source='get_type_display')
    executor_level = ExecutorLevelSerializer()
    category = CategorySerializer()
    status = OrderStatusSerializer()
    customer = UserSerializer()
    executor = UserSerializer()

    class Meta:
        model = Order
        # fields = '__all__'
        fields = ('name', 'description', 'keyword', 'length', 'category', 'customer', 'executor_level', 'executor', 'status')
        read_only_fields = ('executor',)

class OrderCreateSerializer(serializers.ModelSerializer):
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
