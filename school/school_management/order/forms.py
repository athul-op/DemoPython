from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name','date_of_birth','mobile','email','address','age','gender','course','department','purpose','materials']
