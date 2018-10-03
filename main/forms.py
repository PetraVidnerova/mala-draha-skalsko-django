from django import forms

from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text', 'text_en', 'text_de']
        labels = {
            'text': ('Text'),
            'text_en': ('Anglicky'),
            'text_de': ('Německy'),
        }

