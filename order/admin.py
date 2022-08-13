from django.contrib import admin

from .models import Category, ExecutorLevel, OrderStatus, Order, Message, Ticket, Review

admin.site.register(Category)
admin.site.register(ExecutorLevel)
admin.site.register(OrderStatus)
admin.site.register(Order)
admin.site.register(Message)
admin.site.register(Ticket)
admin.site.register(Review)
