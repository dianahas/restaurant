from django import forms
from restaurant.utils import validateString
from Order.models import Order
from Meniu.models import Menu
from django.forms import ModelForm
import datetime 


# class OrderForm(ModelForm):
#     class Meta:
#         model = Order
#         fields = ['name', 'email', 'phone', 'adress', 'status', 'rating']

#     def __init__(self, *args, **kwargs):
#         super(OrderForm, self).__init__(*args, **kwargs)

#         for key in self.fields:
#             self.fields[key].required = True
     
#     def clean(self):
#         cleaned_data = super(OrderForm, self).clean()
#         name = cleaned_data.get('name')
#         adress = cleaned_data.get('adress')
#         rating = cleaned_data.get('rating')

#     def clean_name(self):
#         name = self.cleaned_data.get('name')
#         if validateString(name) == True:
#             return name
#         raise forms.ValidationError("invalid data")

#     def clean_adress(self):
#         adress = self.cleaned_data.get('adress')
#         if validateString(adress) == True:
#             return adress
#         raise forms.ValidationError("invalid data")

#     def clean_rating(self):
#         rating = self.cleaned_data.get('rating')
#         if rating < 0 or rating > 5 :
#             raise forms.ValidationError("invalid data")
#         return rating


class newOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'email', 'phone', 'adress', 'id_menu']

    def __init__(self, *args, **kwargs):
        id_menu = kwargs.pop('id_menu', None)
        today = datetime.date.today()
        super(newOrderForm, self).__init__(*args, **kwargs)
        self.fields['id_menu'].initial = id_menu
        self.fields['id_menu'].widget = forms.HiddenInput()

class codeForm(forms.Form):
    # TODO: Define form fields here
    code = forms.CharField(label='code', max_length=100)
