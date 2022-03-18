from django.urls import path
from .views import (add_user_order, user_open_order, send_request, verify, remove_order_detail, check_out, paid_order,detail_paid_order)


urlpatterns = [
    path('add_user_order', add_user_order),
    path('check_out', check_out, name='check_out'),
    path('open_order', user_open_order, name='user_open_order'),
    path('paid_order', paid_order, name='paid_order'),
    path('detail_paid_order/<order_id>', detail_paid_order, name='detail_paid_order'),
    path('payment', send_request, name='request'),
    path('verify/<order_id>', verify, name='verify'),
    path('remove_order_detail/<detail_id>', remove_order_detail),
]
