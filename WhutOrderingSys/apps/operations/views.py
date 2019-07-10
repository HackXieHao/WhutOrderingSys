from django.shortcuts import render
from .models import Love, Order
from dishes.models import DishInfo
from orderWindows.models import WindowInfo
from .forms import UserOrderForm
from django.http import JsonResponse,HttpResponse
from users.models import DeliveryMan
import  random

# Create your views here.
def user_love(request):
    love_id = request.GET.get('loveid', '')
    love_type = request.GET.get('lovetype','')
    if love_id and love_type:
        if request.user.is_authenticated:
            userLove = Love.objects.filter(love_id=int(love_id), user_id=request.user, love_type=int(love_type))
            if userLove:
                love = userLove[0]
                # 若用户收藏过，则改为取消收藏，此时页面需要显示收藏
                if love.love_status:
                    love.love_status = False
                    love.save()

                    if love_type == 1:
                        # 获取菜品信息，收藏数减1
                        dish = DishInfo.objects.filter(id = int(love_id))[0]
                        dish.love_num -= 1
                        dish.save()
                    elif love_type == 2:
                        # 获取窗口信息，收藏数减1
                        window = WindowInfo.objects.filter(id=int(love_id))[0]
                        window.love_num -= 1
                        window.save()

                    return JsonResponse({'status':'success', 'msg':'收藏'})
                else:
                    love.love_status = True
                    love.save()

                    if love_type == 1:
                        # 获取菜品信息，收藏数加1
                        dish = DishInfo.objects.filter(id=int(love_id))[0]
                        dish.love_num += 1
                        dish.save()
                    elif love_type == 2:
                        # 获取窗口信息，收藏数加1
                        window = WindowInfo.objects.filter(id=int(love_id))[0]
                        window.love_num += 1
                        window.save()

                    return JsonResponse({'status': 'success', 'msg': '取消收藏'})
            else:
                userLove = Love()
                userLove.user_id = request.user
                userLove.love_id = love_id
                userLove.love_type = love_type
                userLove.love_status = True
                userLove.save()

                if love_type == 1:
                    # 获取菜品信息，收藏数加1
                    dish = DishInfo.objects.filter(id=int(love_id))[0]
                    dish.love_num += 1
                    dish.save()
                elif love_type == 2:
                    # 获取窗口信息，收藏数加1
                    window = WindowInfo.objects.filter(id=int(love_id))[0]
                    window.love_num += 1
                    window.save()

                return JsonResponse({'status': 'success', 'msg': '取消收藏'})
        else:
            return JsonResponse({'status':'failed', 'msg':'操作失败，请先登录'})
    else:
        return JsonResponse({'status':'failed', 'msg':'操作失败'})

# 订购功能
def user_order(request, order_id):
    if order_id:
        # print("aaaaaa")
        if request.user.is_authenticated:
            userOrder_form = UserOrderForm(request.POST)
            if userOrder_form.is_valid():
                number = userOrder_form.cleaned_data['number']
                desc = userOrder_form.cleaned_data['desc']
                order_infos = Order.objects.filter(dish_id_id=order_id, user_id=request.user, check_status=0, order_status=1)
                if order_infos:
                    order_info = order_infos[0]
                    order_info.number = order_info.number + number
                    order_info.desc = desc
                    order_info.save()
                else:
                    order_info = Order()
                    order_info.dish_id_id = order_id
                    order_info.user_id = request.user
                    order_info.order_window_id = DishInfo.objects.filter(id = order_id)[0].window_id
                    order_info.check_status = 0
                    order_info.order_status = 1
                    order_info.number = number
                    order_info.desc = desc
                    # 随机生成订单编号
                    order_no = ''
                    for i in range(8):
                        orgin_no = '0123456789'
                        order_no += random.choice(orgin_no)

                    order_info.order_no = order_no

                    # 分配快递员
                    window_id = DishInfo.objects.filter(id=order_id)[0].window_id
                    delivery_man = DeliveryMan.objects.filter(manage_window_id = window_id)[0]
                    order_info.delivery_man = delivery_man

                    order_info.save()
                print("bbbbbb")
                return HttpResponse("<script>alert('订购成功,已加入购物车！');window.location.href='http://127.0.0.1:8000/dishes/dish_detail/" + str(order_id) + "/';</script>")
            else:
                return HttpResponse(
                    "<script>alert('请输入有效的信息！');window.location.href='http://127.0.0.1:8000/dishes/dish_detail/" + str(order_id) + "/';</script>")
        else:
            return HttpResponse(
                "<script>alert('操作失败，请先登录！');window.location.href='http://127.0.0.1:8000/users/user_login/</script>")
    else:
        return HttpResponse(
            "<script>alert('操作失败！');window.location.href='http://127.0.0.1:8000/dishes/dish_detail/" + str(order_id) + "/';</script>")

# 取消订购
def user_cancelorder(request, order_id):
    if order_id:
        if request.user.is_authenticated:
            order_infos = Order.objects.filter(dish_id_id=order_id, user_id=request.user, check_status=0,
                                               order_status=1)
            if order_infos:
                order_info = order_infos[0]
                order_info.order_status = 0
                order_info.save()
                return JsonResponse({'status': 'success', 'msg': '取消订购成功！'})
            else:
                return JsonResponse({'status':'success', 'msg':'您还没有订购该菜品，请先订购！'})
        else:
            return JsonResponse({'status':'failed', 'msg':'操作失败，请先登录！'})
    else:
        return JsonResponse({'status':'error', 'msg':'操作失败！'})


# 订购功能
# def user_order(request):
#     order_id = request.GET.get('order_id', '')
#     if order_id:
#         if request.user.is_authenticated:
#             userOrder = Order.objects.filter(dish_id_id =int(order_id), user_id=request.user)
#             if userOrder:
#                 order = userOrder[0]
#                 # 若已经订购，则此次操作为取消订购，应显示订购
#                 if order.order_status:
#                     order.order_status = False
#                     order.save()
#
#                     # 获取菜品信息，订购数减1
#                     dish = order.dish_id
#                     dish.order_num -= 1
#                     dish.save()
#
#                     return JsonResponse({'status':'success', 'msg':'订购'})
#                 else:
#                     order.order_status = True
#                     order.save()
#
#                     # 获取菜品信息，订购数加1
#                     dish = order.dish_id
#                     dish.order_num += 1
#                     dish.save()
#
#                     return JsonResponse({'status':'success', 'msg':'取消订购'})
#             else:
#                 userorder = Order()
#                 userorder.dish_id_id = order_id
#                 userorder.user_id = request.user
#                 userorder.order_no = order_id
#                 userorder.order_status = True
#                 userorder.save()
#
#                 # 获取菜品信息，订购数加1
#                 dish = userorder.dish_id
#                 dish.order_num += 1
#                 dish.save()
#
#                 return JsonResponse({'status':'success', 'msg':'取消订购'})
#         else:
#             return JsonResponse({'status':'failed', 'msg':'操作失败，请先登录！'})
#     else:
#         return JsonResponse({'status':'failed', 'msg':'操作失败！'})
