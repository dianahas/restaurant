from django import forms
from restaurant.utils import validateString
from Order.models import Order
from Meniu.models import Menu
from django.forms import ModelForm
import datetime 

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

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if validateString(name) == True:
            return name
        raise forms.ValidationError("invalid date")
        
    def clean_adress(self):
        adress = self.cleaned_data.get('adress')
        if validateString(adress) == True:
            return adress
        raise forms.ValidationError("invalid date")


class codeForm(forms.Form):
    # TODO: Define form fields here
    code = forms.CharField(label='code', max_length=100)

    def clean_code(self):
        code = self.cleaned_data.get('code')
        if validateString(code) == False:
            raise forms.ValidationError("invalid date")
        cod = string.split("-")
        if len(cod) != 2:
            raise forms.ValidationError("invalid date")
        try:
            int(cod[0])
            int(cod[1])
        except:
            raise forms.ValidationError("invalid date")
        return code

    
