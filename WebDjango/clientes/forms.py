from django import forms
from .models import Dibujo
from .models import Users
from django.forms import ModelForm

class DibujoForm(forms.ModelForm):
    class Meta:
        model = Dibujo
        fields = "__all__"

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"

