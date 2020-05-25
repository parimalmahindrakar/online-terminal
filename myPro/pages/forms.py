from django import forms
from django.forms import ModelForm, Textarea
from .models import Command


class commandForm(forms.ModelForm):
    class Meta:
        model = Command
        fields = [
            'command'
        ]
        widgets = {
            'command': Textarea(attrs={'cols': 50, 'rows': 1}),
        }
