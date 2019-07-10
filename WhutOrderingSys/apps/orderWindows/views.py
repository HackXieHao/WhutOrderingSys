from django.shortcuts import render
from .models import WindowInfo, WindowType
from dishes.models import DishInfo
from operations.models import Love
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def window_detail_intro(request, window_id):
    if window_id:
        windowinfo = WindowInfo.objects.filter(id=window_id)[0]
        return render(request, 'window-detail-intro.html', {
            'windowinfo':windowinfo,
            'type': 'window_detail_intro',
        })

def window_detail_dishes(request, window_id):
    if window_id:
        windowinfo = WindowInfo.objects.filter(id=window_id)[0]
        dishes = DishInfo.objects.filter(window=windowinfo)
        print(dishes)
        # 分页实现
        page_num = request.GET.get('page', '')
        pa = Paginator(dishes, 4)
        try:
            pages = pa.page(page_num)
        except EmptyPage:
            pages = pa.page(pa.num_pages)
        except PageNotAnInteger:
            pages = pa.page(1)
        return render(request, 'window-detail-dishes.html',{
            'windowinfo': windowinfo,
            'type':'window_detail_dishes',
            'pages':pages
        })

def window_detail(request, window_id):
    if window_id:
        windowinfo = WindowInfo.objects.filter(id=window_id)[0]
        loveWindowStatus = False

        if request.user.is_authenticated:
            userLoveWinodw = Love.objects.filter(love_id=int(window_id), user_id=request.user,
                                                 love_status=True, love_type=2)
            if userLoveWinodw:
                loveWindowStatus = True
        return render(request, 'window-detail-homepage.html', {
            'windowinfo':windowinfo,
            'type': '',
            'loveWindowStatus':loveWindowStatus
        })

def window_list(request):
    # 获取所有窗口类型
    window_types = WindowType.objects.all()

    # 获取所有窗口
    windows = WindowInfo.objects.all()

    # 热度窗口
    hot_window = windows.order_by('-love_num')[:5]

    # 分类实现
    wt = request.GET.get('wt','')
    if wt:
        windows = windows.filter(window_type=int(wt))

    # 排序实现
    sort = request.GET.get('sort','')
    if sort:
        if sort == 'window_no':
            windows = windows.order_by(sort)
        elif sort == 'love_num':
            windows = windows.order_by('-' + sort)


    # 分页实现
    page_num = request.GET.get('page', '')
    pa = Paginator(windows, 5)
    try:
        pages = pa.page(page_num)
    except EmptyPage:
        pages = pa.page(pa.num_pages)
    except PageNotAnInteger:
        pages = pa.page(1)

    return render(request, 'window-list.html', {
        'window_types':window_types,
        'windows':windows,
        'pages':pages,
        'sort':sort,
        'wt':wt,
        'hot_window':hot_window
    })