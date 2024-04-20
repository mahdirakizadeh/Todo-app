from django import forms
from .models import Todo


# class TodoCreateForm(forms.Form):
#     tittle = forms.CharField()
#     body = forms.CharField()
#     created = forms.DateTimeField()


class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'


class TodoUpdateForms(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
