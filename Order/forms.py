from django import forms

from Order.models import Order
from django.forms import ModelForm

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'email', 'phone', 'adress', 'status', 'rating']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].required = True
     
    # def clean(self):
    #     cleaned_data = super(OrderForm, self).clean()
    #     datta = cleaned_data.get('datta')

    # def clean_datta(self):
    #     datta = self.cleaned_data.get('datta')
    #     today = datetime.date.today()
    #     if datta>today:
    #         return datta
    #     raise forms.ValidationError("invalid date")