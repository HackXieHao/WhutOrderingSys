from django.shortcuts import render, redirect, reverse
from dishes.models import DishInfo
from orderWindows.models import WindowInfo
from django.contrib.auth import authenticate, logout, login
from .forms import UserLoginForm, UserRegisterForm,UserManageChangeImage, UserManageChangeInfo,UserManageChangePwd
from users.models import UserInfo
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse,JsonResponse
from operations.models import Order,Love
from django.db.models import Q
# Create your views here.

def index(request):
    dish_infos = DishInfo.objects.all()
    window_infos = WindowInfo.objects.all()

    recomm_img = dish_infos.order_by('-order_num')[:2]

    return render(request, 'index.html',{
        'dish_infos':dish_infos,
        'window_infos':window_infos,
        'recomm_img':recomm_img,
    })

# 注册
def user_register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        user_registerForm = UserRegisterForm(request.POST)
        if user_registerForm.is_valid():
            username = user_registerForm.cleaned_data['username']
            email = user_registerForm.cleaned_data['email']
            password_1 = user_registerForm.cleaned_data['password_1']
            password_2 = user_registerForm.cleaned_data['password_2']
            user_list = UserInfo.objects.filter(Q(student_code=username) | Q(email=email))
            if user_list:
                return render(request, 'register.html', {
                    'msg':'学号或邮箱已注册'
                })
            else:
                if password_1 == password_2:
                    user = UserInfo()
                    user.student_code = username
                    user.username = username
                    user.email = email
                    user.set_password(password_1)
                    user.save()
                    # print("成功")
                    return HttpResponse("<script>alert('注册成功！请尽快登陆前往个人中心完善信息！');window.location.href='http://127.0.0.1:8000/users/user_login/'</script>")
                else:
                    return render(request, 'register.html', {
                        'msg':'两次输入的密码不一致'
                    })
        else:
            return render(request, 'register.html', {
                'user_registerForm':user_registerForm
            })

# 注销
def user_logout(request):
    logout(request)
    return redirect(reverse('index'))

# 登录
def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        user_loginForm = UserLoginForm(request.POST)
        if user_loginForm.is_valid():
            username = user_loginForm.cleaned_data['username']
            password = user_loginForm.cleaned_data['password']

            # user = UserInfo.objects.filter(student_code=username, password=password)
            # if user:
            #     login(request, )
            # user = authenticate(username=username, password=password)
            print(username)
            print(password)
            dj_ps = make_password(password, None, 'pbkdf2_sha256')
            print(dj_ps)
            user = UserInfo.objects.filter(student_code=username)
            if user:
                ps_bool = check_password(password, user[0].password)
                if ps_bool:
                    login(request, user[0])
                    return redirect(reverse('index'))
                else:
                    return render(request, 'login.html', {
                        'msg': '您输入的密码错误'
                    })
            else:
                return render(request, 'login.html', {
                    'msg': '用户名不存在'
                })
        else:
            return render(request, 'login.html', {
                'user_loginForm': user_loginForm
            })

def user_center(request):
    return render(request, 'UserManage/usermanage-info.html')

# 修改头像
def usermanage_changeimage(request):
    usermanage_changeimageForm = UserManageChangeImage(request.POST, request.FILES, instance=request.user)
    if usermanage_changeimageForm.is_valid():
        usermanage_changeimageForm.save(commit=True)
        return JsonResponse({'status':'success'})
    else:
        return JsonResponse({'status':'failed'})

# 修改其他信息
def usermanage_changeinfo(request):
    usermanage_changeinfoForm = UserManageChangeInfo(request.POST,instance=request.user)
    # print(usermanage_changeinfoForm)
    if usermanage_changeinfoForm.is_valid():
        usermanage_changeinfoForm.save(commit=True)
        return HttpResponse("<script>alert('信息更新成功！');window.location.href='http://127.0.0.1:8000/users/user_center/'</script>")
    else:
        return HttpResponse("<script>alert('请将所有信息填写完整！');window.location.href='http://127.0.0.1:8000/users/user_center/'</script>")

def user_changepwd(request):
    userchangepwd_form = UserManageChangePwd(request.POST)
    if userchangepwd_form.is_valid():
        password_1 = userchangepwd_form.cleaned_data['password_1']
        password_2 = userchangepwd_form.cleaned_data['password_2']

        if password_1 == password_2:
            # 更新数据库信息
            user = UserInfo.objects.filter(id=request.user.id)
            if user:
                user[0].set_password(password_1)
                user[0].save()
                return HttpResponse(
                    "<script>alert('密码更新成功！请重新登录！');window.location.href= 'http://127.0.0.1:8000/users/user_login/'</script>")
        else:
            return HttpResponse(
                "<script>alert('两次输入的密码不一致！请重新修改密码！');window.location.href='http://127.0.0.1:8000/users/usercenter_info/'</script>")
    else:
        return HttpResponse(
                "<script>alert('密码输入不合法！请重新修改密码！');window.location.href='http://127.0.0.1:8000/users/usercenter_info/'</script>")

def user_orderInfo(request):
    # 获取用户订单信息
    user_orders = Order.objects.filter(user_id=request.user, order_status=True)
    return render(request, 'UserManage/usermanage-myorder.html',{
        'user_orders':user_orders
    })

def user_lovedish(request):
    # 获取用户收藏菜品信息
    user_loveDishes = Love.objects.filter(user_id=request.user, love_status=True, love_type=1)
    dishes = list()
    if user_loveDishes:
        for love_dish in user_loveDishes:
            dishes.append(DishInfo.objects.filter(id=love_dish.love_id)[0])
    return render(request, 'UserManage/usermanage-love-dish.html',{
        'dishes':dishes
    })

def user_lovewindow(request):
    # 获取用户收藏窗口信息
    user_loveWindowes = Love.objects.filter(user_id=request.user, love_status=True, love_type=2)
    windows = list()
    if user_loveWindowes:
        for love_window in user_loveWindowes:
            windows.append(WindowInfo.objects.filter(id=love_window.love_id)[0])
    return render(request, 'UserManage/usermanage-love-window.html',{
        'windows':windows
    })

# 提交订单
def user_submitorder(request):
    # 获取该用户购物车信息
    user_orders = Order.objects.filter(user_id=request.user, order_status=True)
    # print("aaaaaaa")
    if user_orders:
        for order in user_orders:
            order.order_status = False
            order.check_status = 1
            order.save()

            # 获取菜品id及订购数量
            dish_id = order.dish_id_id
            num = order.number
            # 获取到菜品，并添加订购量
            dish_info = DishInfo.objects.filter(id=dish_id)[0]
            dish_info.order_num += num
            dish_info.save()

        return JsonResponse({'status':'success', 'msg':'订单提交成功'})
            # HttpResponse("<script>alert('订单提交成功！');window.location.href='http://127.0.0.1:8000/users/user_orderInfo/'</script>")
    else:
        return JsonResponse({'status':'failed', 'msg':'您的购物车没有菜品！请前往选择！'})
            # HttpResponse(
            # "<script>alert('您的购物车没有菜品！请前往选择！');window.location.href='http://127.0.0.1:8000/dishes/dish_list'</script>")

# 取消订单
def user_cancelorder(request):
    # 获取该用户购物车信息
    user_orders = Order.objects.filter(user_id=request.user, order_status=False, check_status = 1)
    # print("aaaaaaa")
    if user_orders:
        for order in user_orders:
            order.order_status = True
            order.check_status = 0
            order.save()

            # 获取菜品id及订购数量
            dish_id = order.dish_id_id
            num = order.number
            # 获取到菜品，并减少订购量
            dish_info = DishInfo.objects.filter(id=dish_id)[0]
            dish_info.order_num -= num
            dish_info.save()

        return JsonResponse({'status':'success', 'msg':'订单取消成功！'})
            # HttpResponse(
            # "<script>alert('订单取消成功！');window.location.href='http://127.0.0.1:8000/users/user_orderInfo/'</script>")
    else:
        return JsonResponse({'status':'failed', 'msg':'您暂时还没有提交过订单！'})
            # HttpResponse(
            # "<script>alert('您暂时还没有提交过订单！');window.location.href='http://127.0.0.1:8000/users/user_orderInfo/'</script>")