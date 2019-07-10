from django.shortcuts import render
from .models import DishInfo
from operations.models import Love, Order
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage

# Create your views here.
def dish_detail(request, dish_id):
    if dish_id:
        dishinfo_list = DishInfo.objects.filter(id=dish_id)

        loveStatus = False
        orderStatus = False
        loveWindowStatus = False

        if request.user.is_authenticated:
            userLove = Love.objects.filter(love_id = int(dish_id), user_id=request.user, love_status=True, love_type=1)
            userOrder = Order.objects.filter(dish_id_id=int(dish_id), user_id=request.user, order_status=True)
            userLoveWinodw = Love.objects.filter(love_id=int(dishinfo_list[0].window_id), user_id=request.user, love_status=True, love_type=2)
            if userLove:
                loveStatus = True
            if userOrder:
                orderStatus = True
            if userLoveWinodw:
                loveWindowStatus = True

        if dishinfo_list:
            dishinfo = dishinfo_list[0]
            return render(request, 'dish-detail.html',{
                'dishinfo':dishinfo,
                'loveStatus':loveStatus,
                'loveWindowStatus':loveWindowStatus,
                'orderStatus':orderStatus
            })

def dish_list(request):
    all_dish_infos = DishInfo.objects.all()

    # 热门推荐
    recommend_list = all_dish_infos.order_by('-order_num')[:2]

    # 排序
    type = request.GET.get('sort', '')
    if type:
        all_dish_infos = all_dish_infos.order_by('-' + type)

    # 分页功能实现
    page = request.GET.get('page', '')
    pa = Paginator(all_dish_infos, 6)
    try:
        pages = pa.page(page)
    except PageNotAnInteger:
        pages = pa.page(1)
    except EmptyPage:
        pages = pa.page(pa.num_pages)

    return render(request, 'dish-list.html', {
        'all_dish_infos':all_dish_infos,
        'pages':pages,
        'recommend_list':recommend_list,
        'type':type
    })