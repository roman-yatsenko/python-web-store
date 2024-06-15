from django.urls import path
from django.utils.translation import gettext_lazy as _

from .views import admin_order_detail, order_create

app_name = 'orders'

urlpatterns = [
    path(_('create'), order_create, name='order_create'),
    path('admin/order/<int:order_id>/', admin_order_detail, name='admin_order_detail'),
]
