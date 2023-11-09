from django import forms

class OrderForm(forms.Form):
    date = forms.CharField(max_length=50)
    total = forms.CharField()
    status = forms.CharField(max_length=50)
    address = forms.CharField(max_length=75)

class ProductForm(forms.Form):
    name = forms.CharField(max_length=50)
    price = forms.CharField()
    description = forms.CharField(max_length=50)