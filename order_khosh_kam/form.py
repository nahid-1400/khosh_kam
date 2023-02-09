from django import forms

class OrderForm(forms.Form):
    count = forms.IntegerField(widget=forms.NumberInput(attrs={'margin': '900px', 'min':0}), initial=1)

