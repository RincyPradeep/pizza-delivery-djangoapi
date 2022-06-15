from django.urls import path
from api.v1.orders import views


urlpatterns = [
    path('',views.order_get_view),
    path('create_order/',views.order_create_view),
    path('update_order/<int:order_id>/',views.order_update_view),
    path('delete_order/<int:order_id>/',views.order_delete_view)
]

