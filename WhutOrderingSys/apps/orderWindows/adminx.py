import xadmin
from .models import WindowInfo, WindowType

class WindowTypeXadmin(object):
    list_display = ['name', 'add_time']
    list_editable = ['name']
    search_fields = ['name']
    model_icon = 'fa fa-sitemap'
    show_bookmarks = False

class WindowInfoXadmin(object):
    list_display = ['image', 'window_no', 'name', 'love_num','desc', 'add_time']
    search_fields = ['window_no', 'name']
    list_filter = ['window_no', 'name']
    list_editable = ['window_no', 'name', 'desc']
    model_icon = 'fa fa-windows'
    show_bookmarks = False

xadmin.site.register(WindowType, WindowTypeXadmin)
xadmin.site.register(WindowInfo, WindowInfoXadmin)