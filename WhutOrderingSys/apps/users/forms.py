from django import forms
from .models import UserInfo

class UserLoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=3, max_length=20, error_messages={
        'required': '请填写用户名',
        'min_length': '请输入有效的用户名',
        'max_length': '请输入有效的用户名'
    })
    password = forms.CharField(required=True, min_length=6, max_length=20, error_messages={
        'required': '请填写密码',
        'min_length': '密码不得小于6位',
        'max_length': '密码过长，不得超过20位'
    })

class UserRegisterForm(forms.Form):
    username = forms.CharField(required=True, min_length=3, max_length=20, error_messages={
        'required': '请填写学号',
        'min_length': '请输入有效的用户名',
        'max_length': '请输入有效的用户名'
    })
    email = forms.EmailField(required=True)
    password_1 = forms.CharField(required=True, min_length=6, max_length=20, error_messages={
        'required': '请填写密码',
        'min_length': '密码不得小于6位',
        'max_length': '密码过长，不得超过20位'
    })
    password_2 = forms.CharField(required=True, min_length=6, max_length=20)

class UserManageChangeImage(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['image']

class UserManageChangeInfo(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['student_code', 'name', 'gender', 'phone', 'email', 'address']

class UserManageChangePwd(forms.Form):
    password_1 = forms.CharField(required=True, min_length=6, max_length=20, error_messages={
        'required': '请输入新密码',
        'min_length': '密码不得小于6位',
        'max_length': '密码过长，不得超过20位'
    })
    password_2 = forms.CharField(required=True, min_length=6, max_length=20, error_messages={
        'required': '请再次输入确认密码'
    })
