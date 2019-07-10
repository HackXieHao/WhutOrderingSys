import xadmin
from users.models import DeliveryMan
from xadmin import views

class BaseXadminSettings(object):
    # 添加主题选择功能
    enable_themes = True
    # 添加多个选项到主题选择中
    use_bootswatch = True

class CommonXadminSettings(object):
    site_title = '武汉理工大学订餐后台管理系统'
    site_footer = '万振宇'
    # menu_style = 'accordion'

class DeliveryManXadmin(object):
    list_display = ['name', 'phone', 'manage_window', 'add_time']
    list_filter = ['name', 'manage_window']
    search_fields = ['name', 'manage_window']
    show_bookmarks = False
    model_icon = 'fa fa-user-o'

xadmin.site.register(views.CommAdminView, CommonXadminSettings)
xadmin.site.register(views.BaseAdminView, BaseXadminSettings)
xadmin.site.register(DeliveryMan, DeliveryManXadmin)