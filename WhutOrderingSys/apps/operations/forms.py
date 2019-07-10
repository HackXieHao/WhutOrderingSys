from django import forms

class UserOrderForm(forms.Form):
    number = forms.IntegerField(required=True,min_value=1,error_messages={
        'required': '请填写数量',
        'min_value':'数量最小值为1'
    })
    desc = forms.CharField()