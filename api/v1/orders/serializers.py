from rest_framework import serializers

from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.SerializerMethodField()

    size = serializers.CharField(max_length=20)
    # quantity = serializers.IntegerField()
    order_status = serializers.CharField(default='PENDING')

    class Meta:
        model = Order
        fields = ['id','customer','size','quantity','order_status','created_at','updated_at']

    def get_customer(self,instance):
        return instance.customer.username