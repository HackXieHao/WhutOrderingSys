import xadmin
from .models import DishInfo,WindowInfo

class DishInfoXadmin(object):
    list_display = ['image', 'dish_no', 'name', 'order_num', 'love_num', 'window', 'desc', 'add_time']
    search_fields = ['dish_no', 'name', 'window']
    list_filter = ['dish_no', 'name', 'window']
    list_editable = ['dish_no', 'name', 'window', 'desc']
    model_icon = 'fa fa-free-code-camp'
    show_bookmarks = False


xadmin.site.register(DishInfo, DishInfoXadmin)