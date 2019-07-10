import xadmin
from .models import Order

class OrderXadmin(object):
    list_display = ['order_no', 'dish_id', 'user_id', 'desc','check_status', 'delivery_man', 'add_time']
    search_fields = ['order_no', 'dish_id', 'user_id']
    list_filter = ['order_no', 'order_window_id', 'user_id']
    list_editable = ['check_status']
    show_bookmarks = False
    model_icon = 'fa fa-user-circle-o'

xadmin.site.register(Order, OrderXadmin)