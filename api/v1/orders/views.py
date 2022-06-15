from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import render,get_object_or_404

from orders.models import Order
from api.v1.orders.serializers import OrderSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def order_create_view(request):
    data = request.data
    user = request.user
    serializer = OrderSerializer(data=data)

    if serializer.is_valid():
        serializer.save(customer=user)
        response_data={
            "status" : 6000,
            "data" : serializer.data,
            "message" : "Order created"
        }
    else:
        response_data={
            "status" : 6001,
            "error" : serializer.errors
        }

    return Response(response_data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def order_get_view(request):
    instances = Order.objects.all()
    context = {"request" : request}
    serializer = OrderSerializer(instances,context=context,many=True)

    response_data = {
        "status" : "6000",
        "data" : serializer.data      
    }
    return Response(response_data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def order_update_view(request,order_id):
    data = request.data
    instance = get_object_or_404(Order,pk=order_id)
    context = {"request" : request}
    serializer = OrderSerializer(data=data,instance=instance,context=context)
    if serializer.is_valid():
        serializer.save()
        response_data={
            "status" : 6000,
            "data" : serializer.data,
            "message" : "Order updated"
        }
    else:
        response_data={
            "status" : 6001,
            "error" : serializer.errors,
        }
    return Response(response_data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def order_delete_view(request,order_id):
    instance = get_object_or_404(Order,pk=order_id)

    instance.delete()
    response_data={
        "status":6000,
        "message" : "Order deleted"
    }
    return Response(response_data)