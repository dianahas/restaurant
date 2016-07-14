import datetime 
from django import forms
from django.forms import ModelForm
from restaurant.utils import validateString
from Meniu.models import Menu

class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = ['title', 'datta', 'fel1', 'fel2', 'desert']

    def __init__(self, *args, **kwargs):
        super(MenuForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].required = True
     
    def clean(self):
        cleaned_data = super(MenuForm, self).clean()
        datta = cleaned_data.get('datta')

    def clean_datta(self):
        datta = self.cleaned_data.get('datta')
        today = datetime.date.today()
        if datta>=today:
            return datta
        raise forms.ValidationError("invalid date")

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if validateString(title) == True:
            return title
        raise forms.ValidationError("invalid date")

    def clean_fel1(self):
        fel1 = self.cleaned_data.get('fel1')
        if validateString(fel1) == True:
            return fel1
        raise forms.ValidationError("invalid date")

    def clean_fel2(self):
        fel2 = self.cleaned_data.get('fel2')
        if validateString(fel2) == True:
            return fel2
        raise forms.ValidationError("invalid date")

    def clean_desert(self):
        desert = self.cleaned_data.get('desert')
        if validateString(desert) == True:
            return desert
        raise forms.ValidationError("invalid date")




   